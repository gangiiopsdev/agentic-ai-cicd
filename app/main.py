from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate host to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.strip()}'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}