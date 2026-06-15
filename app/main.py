from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_ping(host)