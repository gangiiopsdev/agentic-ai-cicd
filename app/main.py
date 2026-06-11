from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, args: list[str]):
        full_command = command + ' ' + ' '.join(shlex.quote(arg) for arg in args)
        subprocess.call(full_command, shell=False)

app = FastAPI()

def sanitize_input(input_str):
    # Simple validation example: allow only alphanumeric and a few special characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    sanitized_input = ''.join(char for char in input_str if char in allowed_chars)
    return sanitized_input

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    SafeSubprocess.call('ping', [sanitized_host])
    return {'status': 'completed'}