from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
def execute_ping(host):
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}