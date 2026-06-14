from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    command = ['ping', '--'] + [host]
    subprocess.run(command, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_safe(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    command = ['ping', '--'] + [host]
    subprocess.run(command, check=True)