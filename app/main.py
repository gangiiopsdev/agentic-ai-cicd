from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}