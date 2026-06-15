from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(f'ping {quote(host)}')
    return {'status': 'completed'}