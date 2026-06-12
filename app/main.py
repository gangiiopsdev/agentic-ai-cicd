from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize user input
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}