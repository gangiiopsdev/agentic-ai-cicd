from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Sanitize and validate the host input before executing the command
    if not isinstance(host, str) or not all(c.isalnum() for c in host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}