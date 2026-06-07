from fastapi import FastAPI
import subprocess
import shlex
given_host = host.strip()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(shlex.split(f'ping {given_host}'))
    return {"status": "completed"}