from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host to prevent command injection
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}