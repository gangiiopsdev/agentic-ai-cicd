from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize and validate input
    if not host.strip() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host provided'}
    try:
        args = shlex.split(f'ping -c 1 {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except TimeoutExpired:
        return {'status': 'failed', 'error': 'Ping request timed out'}