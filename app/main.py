from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Simple validation, replace with more robust logic if needed
    return host.replace('.', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}