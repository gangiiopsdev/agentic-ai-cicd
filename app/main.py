from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True)

def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in ['.', '-'] for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}