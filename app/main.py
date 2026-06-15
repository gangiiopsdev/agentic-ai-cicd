from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException

app = FastAPI()

def safe_ping(host):
    if not host.strip().isalnum():
        raise HTTPException(status_code=400, detail="Invalid hostname")
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    try:
        return {'status': 'completed', 'result': safe_ping(host)}
    except HTTPException as e:
        return {'status': 'failed', 'error': e.detail}