from fastapi import FastAPI
import re
import subprocess

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed', 'output': output}