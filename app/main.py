from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Ensure host input is safe
    if 'ping' in host or '&' in host:
        raise ValueError('Unsafe input detected')
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}