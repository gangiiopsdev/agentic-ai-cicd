from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to avoid command injection
    if not host or ' ' in host:
        return {'status': 'error', 'error': 'Invalid host'}
    safe_host = shlex.quote(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}