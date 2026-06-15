from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input
    if not host.isalnum() or '@' in host or ':' in host:
        raise ValueError("Invalid host name")
    # Use a list for the command instead of shell=True
    subprocess.call(['ping', host])

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}