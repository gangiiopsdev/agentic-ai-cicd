from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Host not allowed')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}