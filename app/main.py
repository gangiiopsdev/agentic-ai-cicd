from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        parsed_host = urlparse(host)
        if not parsed_host.hostname:
            raise ValueError('Invalid host format')
        output = subprocess.check_output(['ping', parsed_host.hostname], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}