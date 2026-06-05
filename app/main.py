from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}