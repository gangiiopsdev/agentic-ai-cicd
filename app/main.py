from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains valid characters for a hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', f'--{host}'], check=True)
    return {'status': 'completed'}