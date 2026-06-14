from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        parsed_host = urlparse(host)
        if not all([parsed_host.scheme, parsed_host.netloc]):
            raise ValueError('Invalid host format')
        result = subprocess.check_output(['ping', parsed_host.netloc], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': result}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}