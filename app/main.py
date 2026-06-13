from fastapi import FastAPI
import subprocess

app = FastAPI()

async def validate_host(host):
    valid_hosts = ['example.com', 'localhost']
    return host in valid_hosts

@app.get('/ping')
async def ping(host: str):
    if not await validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', '-c', '1', host]
    result = await subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}