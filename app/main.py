from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize input
        allowed_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        subprocess.run(['ping', '--', host], check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}