from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "invalid_host", "message": "Host not allowed"}