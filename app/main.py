from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

gapp = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = shlex.quote(host)
    subprocess.run(shlex.split(f'ping {safe_host}'))
    return {"status": "completed"}