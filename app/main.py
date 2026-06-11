from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate the input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get('/ping')
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': output}