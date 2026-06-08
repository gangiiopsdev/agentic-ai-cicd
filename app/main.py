from fastapi import FastAPI
import subprocess
import shlex

global host_list
host_list = ['127.0.0.1', '8.8.8.8'] # Replace with actual list of hosts to ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in host_list:
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        return {"error": "Host not allowed"}
    return {"status": "completed"}