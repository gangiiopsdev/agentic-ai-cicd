from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter
    parsed_url = urlparse(host)
    if not parsed_url.hostname:
        return {'status': 'failed', 'error': 'Invalid host format'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}