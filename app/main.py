from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]+-[a-zA-Z0-9]+$', host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}