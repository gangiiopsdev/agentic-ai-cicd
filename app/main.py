from fastapi import FastAPI
import subprocess
import re

async def safe_ping(host: str):
    # Sanitize and validate the host input before executing the command
    if not isinstance(host, str) or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Use a whitelist of allowed hosts or use an alternative method for pinging
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', '-c', '1', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}