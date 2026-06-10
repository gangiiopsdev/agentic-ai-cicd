from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize input
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)
    return {'status': 'completed'}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)