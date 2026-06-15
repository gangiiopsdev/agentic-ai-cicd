from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    # Secure implementation
    if not host.isalnum() and not '.' in host:
        return {'error': 'Invalid host name'}, 400
    try:
        result = subprocess.run(['ping', '-c', '1'], check=True, capture_output=True, text=True, executable='/bin/ping')
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500

global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)