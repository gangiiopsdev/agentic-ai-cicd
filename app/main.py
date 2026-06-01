from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}