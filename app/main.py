from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in host)

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid host name")

app = FastAPI()

@app.get('/')
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}