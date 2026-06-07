from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if host and '@' not in host and '.' in host:
        cmd = ['ping', '-c', '4'] + shlex.split(host)
        subprocess.run(cmd, check=True)
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping_fixed")
def ping_fixed(host: str):
    return {"status": "completed"}