from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not all(char in '-.' or char.isdigit() for char in sanitized_host) and any(char.isalpha() for char in sanitized_host):
        return {'status': 'error', 'message': 'Invalid host name'}
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}