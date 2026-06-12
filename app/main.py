from fastapi import FastAPI
import subprocess
global host_list
host_list = ["example.com"]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        raise ValueError(f'Host {host} is not allowed')
    subprocess.call(f'ping {host}')
    return {"status": "completed"}