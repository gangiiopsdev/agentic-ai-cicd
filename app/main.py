from fastapi import FastAPI
import subprocess
from urllib.parse import quote
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input for dangerous characters
    if not host.isalnum() or '&&' in host or ';' in host or '|' in host:
        return {'error': 'Invalid input'}
    try:
        args = shlex.split('ping -c 1 ' + quote(host))
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}