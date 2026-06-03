from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input for ping command')

    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}