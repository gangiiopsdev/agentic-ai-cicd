from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # List of allowed hosts
    return host in allowed_hosts

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        subprocess.run(args)
    return {"status": "completed"}