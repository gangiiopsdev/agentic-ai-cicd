from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters and escape special shell characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or any(char in host for char in (';', '&', '|', '*', '`')):
        return {'error': 'Invalid host'}, 400

    subprocess.run(['ping', host], check=True, shell=False)

    return {'status': 'completed'}