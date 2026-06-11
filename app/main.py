from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Define a whitelist of allowed hosts or patterns
    allowed_hosts = ['192.168.1.', 'localhost']
    if any(host.startswith(allowed) for allowed in allowed_hosts):
        try:
            result = subprocess.run(['ping', '-c 4', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Unauthorized host'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return await safe_ping(host)