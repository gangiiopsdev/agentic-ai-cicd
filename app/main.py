from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more IPs as needed
    if host not in allowed_hosts:
        raise ValueError(f"Invalid host: {host}")
    command = ['ping', '-c', '4', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}