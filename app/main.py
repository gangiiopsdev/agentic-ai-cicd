from fastapi import FastAPI
import subprocess
import shlex
globally_whitelisted_hosts = set(['example.com', 'test.com']) # Add all allowed hosts here

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_whitelisted_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        raise ValueError('Host not allowed')

    return {"status": "completed"}