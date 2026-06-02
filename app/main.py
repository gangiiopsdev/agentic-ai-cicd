from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host input'}
    try:
        # Secure implementation using subprocess.run with validation and escaping
        subprocess.run(['ping', '-c', '1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}