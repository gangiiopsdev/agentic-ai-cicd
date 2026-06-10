from fastapi import FastAPI
import subprocess
cimport = None
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'status': 'error', 'error': 'Host parameter is required'}
    try:
        # Validate and sanitize the host input
        import re
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'error', 'error': 'Invalid host format'}
        result = subprocess.check_output(['ping', '-c', '1', host], shell=False, input=None)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}