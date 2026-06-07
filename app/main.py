from fastapi import FastAPI
import subprocess
import shlex

global host_list
host_list = []

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not any(host in h for h in host_list):
        subprocess.call(shlex.split(f"ping {host}"))
        host_list.append(host)
    return {"status": "completed"}