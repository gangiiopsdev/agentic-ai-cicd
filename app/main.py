from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            raise ValueError('Invalid character in hostname')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    cmd = ['ping'] + shlex.split(host)
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}