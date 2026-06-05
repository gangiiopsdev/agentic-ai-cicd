from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or '&&' in host or ';' in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True)
    return {"status": "completed"}