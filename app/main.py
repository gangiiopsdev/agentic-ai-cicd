from fastapi import FastAPI
import subprocess
import shlex
import re

class InputSanitizer:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'

    def is_valid(self, input_str: str) -> bool:
        return all(char in self.allowed_chars for char in input_str)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not InputSanitizer().is_valid(host):
        raise ValueError('Invalid host name')

    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}