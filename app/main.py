from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run and sanitizing input
    args = ['ping', '-c', '1'] + [host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is not None:
        return safe_ping(host)
    else:
        return "No host provided"