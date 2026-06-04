from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import List

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shell escaping
    safe_host = ''.join(ch for ch in host if ch.isalnum() or ch in '-_.')
    subprocess.run(['ping', quote(safe_host)], check=True)
    return {'status': 'completed'}