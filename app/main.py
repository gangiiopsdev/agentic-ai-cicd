from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host or len(host) > 128:
        return {"status": "invalid host"}, 400
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}'))
    return {"status": "completed"}