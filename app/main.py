from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host parameter
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid input'}
        output = subprocess.run(['ping', quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}