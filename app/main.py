from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation
    if not host.strip().isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
async def ping(host: str):
    try:
        return ping(host)
    except ValueError as e:
        return {'error': str(e)}