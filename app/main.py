from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate user input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return False
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    if isinstance(output, bool) and not output:
        return {'status': 'failed', 'error': 'Invalid input'}
    else:
        return {'status': 'completed', 'output': output}