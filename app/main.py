from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.run(['ping', host])
    return {"status": "completed"}