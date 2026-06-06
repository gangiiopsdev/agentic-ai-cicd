from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation
    if not host.strip() or len(host) > 100:
        return {'error': 'Invalid host'}, 400
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stdout': e.stdout, 'stderr': e.stderr}, 500
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}