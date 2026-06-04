from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or not all(c.isalnum() or c in '-._' for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}