from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host parameter'}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e}'}