from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'bing.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Secure implementation using subprocess.run with shell=False and passing arguments separately
    command = shlex.split(f'ping -c 4 {host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}