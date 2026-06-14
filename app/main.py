from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely quote the host argument
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    if host and '@' not in host and ':' not in host and '/' not in host:
        # Validate the hostname further to prevent injection
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")
        if all(c in valid_chars for c in host):
            return safe_ping(host)
        else:
            return {'status': 'failed', 'error': 'Invalid hostname'}
    else:
        return {'status': 'failed', 'error': 'Invalid hostname'}