from fastapi import FastAPI
import subprocess
global host_blacklist = set(['127.0.0.1', 'localhost'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in host_blacklist:
        subprocess.call(["ping", host])
    else:
        raise ValueError('Host is blacklisted')
    return {"status": "completed"}