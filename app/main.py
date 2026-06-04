from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate input
    if not host or 'localhost' in host:
        return {'status': 'error', 'message': 'Invalid host'}

    # Secure implementation
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)