from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}