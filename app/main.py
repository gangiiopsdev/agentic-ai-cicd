from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid characters in hostname')
    subprocess.call(['ping', '-c 1', quote(sanitized_host)], shell=False)
    return {'status': 'completed'}