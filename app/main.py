from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, text=True, capture_output=True)
    return {"status": "completed", "output": result.stdout}