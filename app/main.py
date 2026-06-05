from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

.globally_allowed_hosts = {"example.com", "localhost"}

app = FastAPI()

def is_safe_host(host):
    parsed_host = urlparse(host)
    return parsed_host.netloc in globally_allowed_hosts

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        return safe_ping(host)
    else:
        raise ValueError("Host not allowed")