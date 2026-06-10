from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

def is_safe_command(command, args):
    safe_commands = ['ping']
    return command == 'ping' and all(arg.isalnum() or arg.startswith('-') for arg in args)

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    if is_safe_command('ping', [sanitized_host]):
        try:
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid command or argument'}