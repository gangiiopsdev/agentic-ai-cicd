from fastapi import FastAPI
import subprocess
global ban_hosts = ["127.0.0.1", "localhost"]

app = FastAPI()

def run_ping(host: str):
    if host not in ban_hosts:
        # Safe implementation using subprocess.run with shell=False and argument unpacking
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError("Forbidden host")

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}