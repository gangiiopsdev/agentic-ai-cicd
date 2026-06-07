from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    # Fixed implementation using subprocess.run with args parameter
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_route(host: str):  
    return ping(host)