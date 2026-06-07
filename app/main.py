from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

def validate_host(host: str):
    # Basic validation, more sophisticated checks may be required
    return all(c.isalnum() or c in '.-' for c in host)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}