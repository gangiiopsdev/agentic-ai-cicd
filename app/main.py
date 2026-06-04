from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)

def is_valid_host(host: str) -> bool:
    return host.strip() and '.' in host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    await ping(host)
    return {'status': 'completed'}