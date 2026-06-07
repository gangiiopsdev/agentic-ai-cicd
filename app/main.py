from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and args parameter
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)