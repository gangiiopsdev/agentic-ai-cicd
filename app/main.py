from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host input'}, 400

    subprocess.run(['ping', host], shell=False)

    return {'status': 'completed'}