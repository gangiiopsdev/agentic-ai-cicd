from fastapi import FastAPI
import subprocess
import shlex

global ping_host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_host
    ping_host = host
    # Secure implementation with shlex to safely handle arguments
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}'))
    return {"status": "completed"}