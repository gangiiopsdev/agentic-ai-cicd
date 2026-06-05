from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}