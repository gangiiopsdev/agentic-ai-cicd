from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'invalid', 'message': 'Invalid host'}
    return _ping(host)