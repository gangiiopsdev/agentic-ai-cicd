from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '.' not in host:
        return {"status": "invalid_host"}, 400
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}