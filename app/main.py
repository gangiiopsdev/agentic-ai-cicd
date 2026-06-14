from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not host.isalnum():
        return {'error': 'Invalid host'}, 400
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e.stderr.decode()}'}, 500