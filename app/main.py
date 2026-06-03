from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not all(c.isalnum() or c in [',', '.', '-'] for c in host):
        raise ValueError('Invalid host input')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}