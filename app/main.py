from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in safe_chars for char in hostname)

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'invalid_host'}
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}