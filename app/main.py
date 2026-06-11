from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def ping_safe(host: str):
    # Ensure the host does not contain any malicious characters
    parsed_host = urlparse(host)
    if not parsed_host.hostname:
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.run(['ping', '-c', '1', parsed_host.hostname], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)