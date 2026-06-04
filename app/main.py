from fastapi import FastAPI
import subprocess

app = FastAPI()

async def is_safe_host(host):
    # Implement logic to check if host is safe
    return 'allowed_host' == host

@app.get('/ping')
def ping(host: str):
    if not await is_safe_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}