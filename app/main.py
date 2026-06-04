from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        host = shlex.quote(host)
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}