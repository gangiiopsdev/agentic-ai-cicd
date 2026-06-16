from fastapi import FastAPI
import subprocess
import re

def run_ping(host: str):
    # Validate the input to ensure it only contains allowed characters (e.g., alphanumeric, hyphen)
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return run_ping(host)