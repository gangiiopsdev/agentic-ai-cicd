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
    command = f'ping {shlex.quote(host)}'
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {
        "status": "completed",
        "output": result.stdout,
        "errors": result.stderr
    }