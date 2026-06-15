from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    # Secure implementation using subprocess.run with argument list
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'status': 'completed', 'message': 'Ping successful'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize input
        if not host.isalnum() or len(host) > 255:
            raise ValueError('Invalid host name')
        # Secure implementation using subprocess.run with argument list
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'status': 'completed', 'message': 'Ping successful'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}