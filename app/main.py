from fastapi import FastAPI
import subprocess
import shlex
import re

class InputFilter:
    def __init__(self):
        self.allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')

    def sanitize(self, input_str: str) -> str:
        return ''.join(c for c in input_str if c in self.allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    filter_instance = InputFilter()
    sanitized_host = filter_instance.sanitize(host)
    if not sanitized_host:
        return {'error': 'Invalid host name'}
    try:
        subprocess.run(['ping', '-c 1', f'"{sanitized_host}"'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}