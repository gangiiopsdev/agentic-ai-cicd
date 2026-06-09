from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run with proper escaping and validation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c', '4', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}