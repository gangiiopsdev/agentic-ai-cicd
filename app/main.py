from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}