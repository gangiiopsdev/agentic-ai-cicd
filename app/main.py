from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}