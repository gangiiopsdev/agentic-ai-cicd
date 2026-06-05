from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    return hostname.isalnum() and len(hostname) <= 64

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "error", "message": "Invalid host name"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}