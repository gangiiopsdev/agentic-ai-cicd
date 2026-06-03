from fastapi import FastAPI
import subprocess
global host whitelist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_host_whitelist:
        subprocess.call(f'ping {host}', shell=True)
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}