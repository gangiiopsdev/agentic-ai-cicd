from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent code injection
    if not host.isdigit() or len(host) > 3:
        return {"error": "Invalid host"}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args)
    return {"status": "completed"}