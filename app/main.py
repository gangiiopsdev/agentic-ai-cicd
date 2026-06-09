from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the input using shlex.quote to handle special characters safely
    sanitized_host = quote(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)