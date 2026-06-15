from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isdigit() and '@' not in host:
        return {'status': 'invalid_host'}
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}