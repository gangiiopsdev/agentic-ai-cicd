from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c.isdigit())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {"status": "completed"}