from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to allow only alphanumeric characters, hyphens, and dots
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    try:
        subprocess.run(['ping', shlex.quote(host)], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500