from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}