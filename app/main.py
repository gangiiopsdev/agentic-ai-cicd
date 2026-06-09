from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    return re.match('^[a-zA-Z0-9.-]+$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid input for ping command')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}