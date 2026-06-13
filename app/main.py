from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host parameter
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        args = ['ping', shlex.quote(host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}