from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host parameter'}

    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}