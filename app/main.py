from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    command_parts = ['ping', shlex.quote(host)]
    subprocess.call(command_parts)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    command_parts = ['ping', shlex.quote(host)]
    subprocess.call(command_parts)
    return {"status": "completed"}