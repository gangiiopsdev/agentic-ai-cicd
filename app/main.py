from fastapi import FastAPI
import subprocess
import re
import shlex
def safe_ping(host: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(c in allowed_chars for c in host):
        return False
    # Regex to validate the input further
    if re.match(r'^[a-zA-Z0-9.-_]+$', host) is None:
        return False
    args = ['ping', shlex.quote(host)]
    try:
        subprocess.run(args, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        return False
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        raise ValueError('Invalid input')
    return {'status': 'completed'}