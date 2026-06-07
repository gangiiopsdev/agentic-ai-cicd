from fastapi import FastAPI
import subprocess
import shlex

async def secure_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    response = secure_ping(host)
    return {'status': 'completed', 'output': response}

def validate_host(host: str) -> bool:
    # Implement input validation logic here
    allowed_hosts = ['example.com']  # Example allowed hosts
    return host in allowed_hosts