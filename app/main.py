from fastapi import FastAPI
import subprocess
global host_list = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        host_list.add(host)
        subprocess.call(f'ping -c 4 {host}', shell=False)
    return {"status": "completed"}