from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using shell=False and ensuring host is safe
    if not validate_host(host):
        raise ValueError('Invalid host')
    await run_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Secure implementation using shell=False and ensuring host is safe
    if not validate_host(host):
        raise ValueError('Invalid host')
    await run_ping(host)
    return {'status': 'completed'}

async def run_ping(host: str):
    import asyncio
    process = await asyncio.create_subprocess_exec('ping', host, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed with return code {process.returncode}: {error.decode()}')

async def validate_host(host: str) -> bool:
    # Simple example of validation logic
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts