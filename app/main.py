from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}