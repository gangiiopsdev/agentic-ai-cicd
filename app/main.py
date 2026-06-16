from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts