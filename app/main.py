from fastapi import FastAPI
import subprocess
import shlex
import os

def ping(host: str):
    # Safe implementation
    if not os.path.exists('/bin/ping'):
        return {"error": "ping command not found"}
    args = shlex.split('ping ' + host)
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if not os.path.exists('/bin/ping'):
        return {"error": "ping command not found"}
    args = shlex.split('ping ' + host)
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}