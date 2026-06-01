from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote

app = FastAPI()

def secure_shell_command(command_parts):
    if any(char in command_parts for char in [';', '&', '|', '>', '<', '*', '?', '{', '}', '~', '`']):
        raise ValueError('Unsafe characters detected in command input')

@app.get('/ping')
def ping(host: str):\n    # Secure implementation
    try:\n        args = [quote(arg) for arg in shlex.split(f'ping {host}')]
        secure_shell_command(args)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': e.stderr}