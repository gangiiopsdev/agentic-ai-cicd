from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host.replace('.', '').isnumeric() and len(sanitized_host.split('.')) == 4:
        subprocess.call(['ping', sanitized_host])
    else:
        return {'error': 'Invalid host format'}
    return {'status': 'completed'}