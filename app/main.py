from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host input (e.g., check for allowed characters and length)
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400