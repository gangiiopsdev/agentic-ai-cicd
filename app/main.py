from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()
@app.get="/ping")
def ping(host: str):    
    safe_ping(host)
    return {"status": "completed"}