from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter
    if not host or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host format'}

    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}