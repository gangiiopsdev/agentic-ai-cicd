from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def execute_ping(host: str) -> str:
    if not host:
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)