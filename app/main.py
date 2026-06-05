from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host == 'localhost':
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host provided')
    return {'status': 'completed'}