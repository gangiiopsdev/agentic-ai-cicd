from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host and '-' not in host and len(host) <= 15:
        subprocess.call(['ping', '-c', '4', quote(host)])
    return {'status': 'completed'}