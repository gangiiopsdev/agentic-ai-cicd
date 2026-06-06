from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.strip().endswith('.com') or len(host.split('.')) != 3:
        raise ValueError('Invalid hostname format')
    safe_host = shlex.quote(host)
    subprocess.call(['ping', '-c', '4', safe_host])
    return {"status": "completed"}