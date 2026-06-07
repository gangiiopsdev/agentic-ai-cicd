from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or '.' not in host:
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}