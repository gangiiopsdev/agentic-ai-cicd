from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate host input to avoid command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)