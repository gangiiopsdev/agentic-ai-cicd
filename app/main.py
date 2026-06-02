from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip().isalnum():
        raise ValueError('Invalid hostname')
    safe_host = host.replace('.', '_').replace('-', '_')
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}