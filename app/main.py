from fastapi import FastAPI
import subprocess
import shlex
def shell_escape(s):
    return ''.join([c if c.isalnum() or c in '._-:/\' else \\u%04x' % ord(c) for c in s])

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:/_')
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = ['ping'] + shlex.split(shell_escape(host))
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}