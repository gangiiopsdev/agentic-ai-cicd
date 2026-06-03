from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Command timed out'}