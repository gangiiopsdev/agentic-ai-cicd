from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        cmd = ['ping'] + shlex.split(host)
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}