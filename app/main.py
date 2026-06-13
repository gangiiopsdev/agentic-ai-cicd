from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def is_safe_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and not parsed_url.netloc.startswith('127.0.0.1')

@app.get("/ping")
def ping(host: str):
    if is_safe_url(host):
        # Secure implementation with additional checks
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}