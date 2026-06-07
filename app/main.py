from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and argument list
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum() or '-' not in host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return await ping(host)