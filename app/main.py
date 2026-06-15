from fastapi import FastAPI
import subprocess
import shlex

global ping_hosts
ping_hosts = {'google.com', 'example.com'}

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ping_hosts:
        subprocess.call(shlex.split(f"ping {host}"))
    else:
        return {"error": "Invalid host"}
    return {"status": "completed"}