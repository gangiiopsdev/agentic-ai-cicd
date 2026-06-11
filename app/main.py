from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            sanitized_host = shlex.quote(host)
            result = subprocess.run(['ping', '-c', '4', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)