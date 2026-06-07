from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}