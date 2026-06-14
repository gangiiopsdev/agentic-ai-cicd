from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host and '.' in host:
        args = ['ping', host]
        subprocess.run(args, check=True)
    else:
        raise ValueError('Invalid host')

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}