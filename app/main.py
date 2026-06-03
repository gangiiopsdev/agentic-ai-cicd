from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping'] + shlex.split(host), universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

async def is_valid_host(host: str) -> bool:
    # Simple validation example, replace with actual logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping_safe')
def ping_safe(host: str):
    return await ping(host)