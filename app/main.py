from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed', 'output': output.decode('utf-8')}