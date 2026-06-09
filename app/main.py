from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9._-]+$', host) or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid host'}

    try:
        args = ['ping', '-c', '4', shlex.quote(host)]  # Use shlex.quote to sanitize the input
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}