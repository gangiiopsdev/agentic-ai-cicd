from fastapi import FastAPI
import re
import socket
import subprocess

app = FastAPI()

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host provided."}
    return safe_ping(host)