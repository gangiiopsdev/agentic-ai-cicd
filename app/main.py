from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    return host.replace('.', '').isdigit()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Sanitize host input to prevent shell injection
        safe_host = shlex.quote(host)
        output = subprocess.check_output(['ping', '-c', '4', safe_host], stderr=subprocess.STDOUT, text=True, shell=False)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}