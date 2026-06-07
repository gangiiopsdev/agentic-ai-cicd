from fastapi import FastAPI
import subprocess
global allowed_hosts = ['host1', 'host2']  # Define a list of allowed hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        subprocess.call(f"ping {{host}}", shell=False)  # Use shell=False to prevent command injection
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized access attempt"}