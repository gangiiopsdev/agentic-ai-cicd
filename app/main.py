from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        command = shlex.split('ping ' + host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}