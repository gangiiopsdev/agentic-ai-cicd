from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host or not host.strip().isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}