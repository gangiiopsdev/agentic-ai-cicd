from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Improved input validation
    if not re.match(r'^[a-zA-Z0-9]{1,100}$', host):
        return {'status': 'error', 'message': 'Invalid host name'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}