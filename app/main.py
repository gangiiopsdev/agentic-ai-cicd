from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def safe_ping(host: str):
    try:
        parsed_host = urlparse(host)
        if parsed_host.scheme or ':' in host.split('/')[0]:
            raise ValueError('Invalid host format')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}