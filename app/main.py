from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def safe_ping(host: str):
    try:
        parsed_url = urlparse(host)
        if parsed_url.scheme or '/' in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)