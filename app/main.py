from fastapi import FastAPI
import subprocess
import shlex
global_host = "example.com"  # Replace with actual host

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(command)
    return {"status": "completed"}