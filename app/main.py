from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts check
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}