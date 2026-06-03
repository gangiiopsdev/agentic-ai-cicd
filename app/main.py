from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or 'ping' not in host:
        raise ValueError('Invalid host')
    # Sanitize the host input to prevent command injection
    host = shlex.quote(host)
    return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}