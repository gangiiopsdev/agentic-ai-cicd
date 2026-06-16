from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    cmd = shlex.split(f'ping {host}')
    sanitized_host = subprocess.quote(host)
    full_cmd = f'ping {sanitized_host}'
    subprocess.run(full_cmd, check=True, shell=True)
    return {"status": "completed"}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(cmd, check=True)
    return {"status": "completed"}