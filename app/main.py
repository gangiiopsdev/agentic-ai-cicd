from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input
    if not host.isalnum() or '-' not in host:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)