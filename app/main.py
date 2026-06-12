from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    # Secure implementation
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}