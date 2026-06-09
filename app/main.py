from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.strip() or not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}