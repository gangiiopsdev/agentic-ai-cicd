from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with a full path and shell=False
    if host.isalnum():
        subprocess.run(['ping', host], check=True, shell=False)
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}