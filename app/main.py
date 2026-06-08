from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Ensure host is a valid IP or domain name to avoid shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    subprocess.run(["ping", host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}