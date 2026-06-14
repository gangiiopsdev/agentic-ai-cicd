from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only specific hosts for safety
        subprocess.call(['ping', host])
    else:
        raise ValueError('Unauthorized ping request')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}