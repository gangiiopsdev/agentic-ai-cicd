from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def safe_ping(host: str):
    try:
        parsed_host = urlparse(host)
        if parsed_host.scheme or '@' in host or '%' in host:
            raise ValueError('Invalid host name')
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode().strip()}'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}