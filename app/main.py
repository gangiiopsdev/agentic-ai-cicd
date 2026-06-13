from fastapi import FastAPI
import subprocess
import re
def run_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):  # Updated regex for more comprehensive validation
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return run_ping(host)