from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    safe_ping(host)
    return {"status": "completed"}