from fastapi import FastAPI
import subprocess
import shlex
globally_safe_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in globally_safe_hosts:
        raise ValueError("Invalid host")
    subprocess.run(shlex.split(f'ping {host}'), check=True, shell=False)
    return {"status": "completed"}