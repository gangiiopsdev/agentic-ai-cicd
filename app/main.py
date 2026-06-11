from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '&&' in host or ';' in host or '|' in host:
        raise ValueError('Invalid host input')

    # Secure implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}