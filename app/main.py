from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Secure implementation using subprocess.Popen
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    try:
        await asyncio.create_subprocess_exec(*args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    try:
        await asyncio.create_subprocess_exec(*args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def is_valid_host(host: str) -> bool:
    # Example validation logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts