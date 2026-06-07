from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(filter(str.isalnum, host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host or ' ' in sanitized_host:
        raise ValueError('Invalid host name')
    subprocess.call(shlex.split(f'ping {sanitized_host}'))