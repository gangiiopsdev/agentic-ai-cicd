from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host input')
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping_endpoint(host: str):
    return secure_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}