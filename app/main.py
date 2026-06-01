from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in hostname)

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(shlex.split(f'ping {safe_host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}