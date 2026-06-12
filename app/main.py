from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    escaped_host = quote(host)
    try:
        result = subprocess.run(['ping', '-c 1', escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)