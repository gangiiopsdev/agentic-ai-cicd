from fastapi import FastAPI
import subprocess
global _ping_hosts_allowed
_ping_hosts_allowed = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in _ping_hosts_allowed:
        raise ValueError(f'Host {host} is not allowed to be pinged')
    subprocess.call(['ping', host])
    return {"status": "completed"}