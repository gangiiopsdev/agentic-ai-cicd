from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = {'192.168.0.1', '10.0.0.1'}

async def safe_ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
async def ping(host: str):
    return await safe_ping(host)