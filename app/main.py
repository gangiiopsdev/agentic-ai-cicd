from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if ' ' in host or '\' in host:
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}