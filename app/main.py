from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host or ' ' in host:
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}