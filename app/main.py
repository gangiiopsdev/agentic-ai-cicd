from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str) -> dict:
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    # Sanitize the host parameter to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    args = ['ping', '-c', '1', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
async def ping(host: str):
    # Validate host input further to ensure it is safe before passing to subprocess
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return await safe_ping(host)