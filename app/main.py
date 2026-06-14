from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Validate the host input to prevent injection attacks
    if not host.strip() or not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)