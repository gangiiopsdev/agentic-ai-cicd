from fastapi import FastAPI
import subprocess
global_hosts = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        subprocess.call(['ping', host])
    else:
        return {'status': 'not allowed'}