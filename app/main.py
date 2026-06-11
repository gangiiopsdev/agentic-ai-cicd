from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to ensure it does not contain malicious data
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        return {'status': 'failed', 'error': 'Invalid host parameter'}
    try:
        args = shlex.split(f'ping --no-fail {host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}