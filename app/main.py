from fastapi import FastAPI
import subprocess
global host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global host
    host = host.strip()
    if not host:
        raise ValueError('Host cannot be empty')
    safe_host = subprocess.list2cmdline([host])  # Sanitize the host input
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {"status": "completed", "host": host}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}