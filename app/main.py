from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to avoid injection attacks
    if not all(c.isalnum() or c == '-' for c in host) or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}