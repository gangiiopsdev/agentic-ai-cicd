from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', '-c', '4', host])
    return {'status': 'completed'}