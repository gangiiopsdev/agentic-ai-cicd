from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host or not host.strip():
        raise ValueError('Invalid host')
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return await ping(host)