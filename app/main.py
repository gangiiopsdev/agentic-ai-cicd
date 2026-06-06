from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['example.com', 'test.net']
    if host not in valid_hosts:
        raise ValueError('Invalid host')
    try:
        # Use shell=False and split command to avoid injection attacks
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in ['example.com', 'test.net']:
        return {'error': 'Invalid host'}
    return safe_ping(host)