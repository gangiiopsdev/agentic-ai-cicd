from fastapi import FastAPI
import subprocess
def execute_safe_ping(host: str):
    # Safe implementation using list for arguments and validating input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host format')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_ping(host)
    return {"status": "completed"}