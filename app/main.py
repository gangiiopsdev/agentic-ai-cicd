from fastapi import FastAPI
import subprocess
import re
def ping(host: str):
    # Sanitize host input to prevent injection attacks
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    try:
        output = subprocess.check_output(['ping', '--'], [sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return ping(host)