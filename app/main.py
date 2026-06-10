from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not host:
        return {'status': 'error', 'message': 'Host parameter is required'}
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid characters in host parameter'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}