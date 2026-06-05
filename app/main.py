from fastapi import FastAPI
import subprocess
from shlex import quote


def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's safe to ping
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return safe_ping(host)