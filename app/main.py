from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper validation
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        subprocess.run(['ping', '-c 1', host], check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403