from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Invalid host provided')
    # Secure implementation
    subprocess.run(['ping', '-c 1', host], check=True, capture_output=True)
    return {'status': 'completed'}