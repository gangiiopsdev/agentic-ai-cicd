from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400