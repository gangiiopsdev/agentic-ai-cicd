from fastapi import FastAPI
import subprocess
import re

def run_ping(host):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9-.]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        output = subprocess.check_output(['ping', '-c', str(4), host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(host)