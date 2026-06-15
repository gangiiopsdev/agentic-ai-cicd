from fastapi import FastAPI
import subprocess
global allowed_hosts = {'example.com', 'localhost'}

def is_host_allowed(host):
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_host_allowed(host):
        raise Exception("Unauthorized host")
    subprocess.call(f'ping {host}', shell=True)
    return {"status": "completed"}