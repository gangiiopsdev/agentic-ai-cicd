from fastapi import FastAPI
import subprocess
import socket
def is_valid_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(f"ping {host}", shell=False)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}