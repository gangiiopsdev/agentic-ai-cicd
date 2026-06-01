from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip() and all(c.isalnum() or c in ('-', '.', '_', ':', '/', '@') for c in host):
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        return {"status": "invalid input"}
    return {"status": "completed"}