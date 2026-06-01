from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}