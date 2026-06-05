from fastapi import FastAPI
import subprocess
import shlex
def is_safe_hostname(hostname: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in hostname)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings for security
    subprocess.run(args, check=True)
    return {'status': 'completed'}