from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize and validate the input
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return ping(host)