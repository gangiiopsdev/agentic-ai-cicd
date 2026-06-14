from fastapi import FastAPI
import subprocess
import shlex
import os

def ping(host: str):
    # Sanitize user input
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {"error": "Invalid host parameter"}
    
    if not os.path.exists('/bin/ping'):
        return {"error": "ping command not found"}
    args = shlex.split('ping ' + shlex.quote(host))
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
    # Sanitize user input
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {"error": "Invalid host parameter"}
    
    if not os.path.exists('/bin/ping'):
        return {"error": "ping command not found"}
    args = shlex.split('ping ' + shlex.quote(host))
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}