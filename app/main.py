from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = ['ping', 'host']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {"status": "completed"}