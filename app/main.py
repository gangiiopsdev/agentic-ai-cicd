from fastapi import FastAPI
import subprocess
import shlex
class SanitizedCommand:
    def __init__(self, command: str):
        self.command = shlex.quote(command)

    def execute(self, *args, **kwargs):
        return subprocess.check_output([self.command] + list(args), stderr=subprocess.STDOUT, **kwargs)
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(allowed_chars.__contains__, input_string))
def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    sanitized_host = sanitize_input(host)
    try:
        output = SanitizedCommand('ping').execute(sanitized_host, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}