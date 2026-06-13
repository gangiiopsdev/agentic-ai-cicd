from fastapi import FastAPI
import subprocess
global ping_host_whitelist = set(['127.0.0.1', '::1'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ping_host_whitelist:
        raise ValueError('Host not allowed')
    subprocess.call(f'ping {host}')
    return {"status": "completed"}