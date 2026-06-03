from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
    else:
        return {"status": "error", "message": "Invalid host"}
    return {"status": "completed"}