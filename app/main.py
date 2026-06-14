from fastapi import FastAPI
import subprocess
global_hosts = {'example.com', 'localhost'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in global_hosts:
        raise ValueError('Invalid host')
    subprocess.call(f'ping {host}', shell=False)
    return {"status": "completed"}