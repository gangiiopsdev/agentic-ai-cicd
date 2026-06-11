from fastapi import FastAPI
import subprocess
import shlex
import re

class InputValidator:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'

    def validate(self, host: str) -> bool:
        return all(char in self.allowed_chars for char in host)

app = FastAPI()

input_validator = InputValidator()

def ping(host: str):
    if not input_validator.validate(host):
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}