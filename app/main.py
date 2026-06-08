from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid host name'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}