from fastapi import FastAPI
import subprocess
global allowed_hosts
allowed_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

def validate_host(host):
    global allowed_hosts
    if host in allowed_hosts:
        return True
    else:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global allowed_hosts
    if validate_host(host):
        subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid host")

    return {"status": "completed"}