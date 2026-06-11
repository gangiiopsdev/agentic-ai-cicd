from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize host input
    allowed_hosts = ['example.com', 'test.net']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    ping_command = ['ping', host]
    subprocess.run(ping_command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}