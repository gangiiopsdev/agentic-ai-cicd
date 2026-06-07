from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in hostname:
        if char not in allowed_chars or len(hostname) > 255:
            return False
    return True

@app.get('/ping')
def ping(host: str):
    if not safe_hostname(host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}