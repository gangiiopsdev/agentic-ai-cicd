from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host input is sanitized or validated
    if not all(c.isalnum() or c in [',', '.', '-', '_', ' '] for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)