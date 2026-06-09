from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {"error": "Host not allowed"}, 403
    command = shlex.split(f'ping -c 1 {host}')
    try:
        subprocess.run(command, check=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": f'Ping failed: {e}'}, 500

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {"error": "Host not allowed"}, 403
    command = shlex.split(f'ping -c 1 {host}')
    try:
        subprocess.run(command, check=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": f'Ping failed: {e}'}, 500