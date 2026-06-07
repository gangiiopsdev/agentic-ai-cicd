from fastapi import FastAPI
import subprocess
import shlex
global host_list
host_list = ['127.0.0.1']
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        return {'error': 'Invalid host'}
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {"status": "completed"}