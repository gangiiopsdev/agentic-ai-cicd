from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}