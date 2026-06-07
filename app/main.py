from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', subprocess.check_output(['echo', host]).decode().strip()]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}