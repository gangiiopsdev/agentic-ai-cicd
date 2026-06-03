from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)  # Ensure shell=False
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}