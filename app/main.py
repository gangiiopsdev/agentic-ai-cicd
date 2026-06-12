from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host not in ['localhost', '127.0.0.1']:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}