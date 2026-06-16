from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        # Safe to ping numeric IP addresses
        subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host format')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}, 400
    return {"status": "completed"}