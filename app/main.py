from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with full path and input validation
    if not host.startswith('192.168.'):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['/bin/ping', host], check=True)
    return {'status': 'completed'}