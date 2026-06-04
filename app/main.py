from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid characters in host")

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}