from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_host(host))
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}