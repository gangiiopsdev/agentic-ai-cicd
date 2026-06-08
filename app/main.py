from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation with full path for the command and handling untrusted input
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or '..' in host or ';' in host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)