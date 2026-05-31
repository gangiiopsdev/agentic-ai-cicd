from fastapi import FastAPI
import subprocess
from urllib.parse import quote
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with additional validation and sanitization
    if '&&' in host or ';' in host or '|' in host:
        return {'error': 'Invalid input'}
    try:
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}