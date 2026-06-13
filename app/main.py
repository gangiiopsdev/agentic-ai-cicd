from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Safe implementation using a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}