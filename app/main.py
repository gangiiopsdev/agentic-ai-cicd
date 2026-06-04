from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        # Sanitize input to prevent command injection
        host = shlex.quote(host)
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}