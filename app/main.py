from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() for c in host) or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        # Safe implementation using subprocess.run and list arguments
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)