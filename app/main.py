from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

globally_allowed_hosts = {"example.com", "localhost"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    parsed_host = urlparse(host)
    if parsed_host.netloc in globally_allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.stderr.decode()}
    else:
        raise ValueError("Host not allowed")