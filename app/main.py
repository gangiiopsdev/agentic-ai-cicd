from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        # Validate host before using subprocess
        if not validate_host(host):
            raise ValueError('Invalid host')
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return await ping(host)

async def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Define allowed hosts
    return host in allowed_hosts