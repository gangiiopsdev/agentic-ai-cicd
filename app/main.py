from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or use a different approach to avoid command execution
        if host not in ['allowed_host1', 'allowed_host2']:
            raise ValueError('Host not allowed')
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    # Ensure host input is sanitized to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)