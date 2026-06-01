from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    allowed_hosts = ['example.com', 'test.com']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}