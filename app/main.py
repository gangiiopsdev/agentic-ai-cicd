from fastapi import FastAPI
import shlex
import os

app = FastAPI()

def run_ping(host: str):
    try:
        # Use a whitelist approach to sanitize the input
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
        sanitized_host = ''.join(e for e in host if e in allowed_chars)
        result = subprocess.run(['ping', '-c', str(4), sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    if '/' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)