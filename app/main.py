from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in host:
        if char not in allowed_chars:
            raise ValueError('Invalid characters in host name')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}