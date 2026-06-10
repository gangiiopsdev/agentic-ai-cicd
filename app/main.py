from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    subprocess.run(['ping', host], check=True, shell=False)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)