from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not host or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        cmd = ['ping', '-c', '4'] + shlex.split(host)
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}