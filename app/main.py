from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '.' in host:
        return {"status": "error", "message": "Invalid host input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}