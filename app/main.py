from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {"status": "invalid_host"}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}