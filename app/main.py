from fastapi import FastAPI
import subprocess
global allowed_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        subprocess.call(f'ping {host}', shell=True)
    else:
        raise Exception('Host not allowed')
    return {"status": "completed"}