from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation
    ping_command = ['ping', f'-c 4 {host}']
    subprocess.run(ping_command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure host input is sanitized
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host input')
    safe_ping(host)
    return {"status": "completed"}