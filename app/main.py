from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Invalid or missing host')
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed'}