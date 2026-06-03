from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' not in host:
        raise ValueError('Invalid host')
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}