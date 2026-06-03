from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum() or len(input_str) > 255:
        return False
    for char in shlex.split(input_str):
        if any(char.startswith(char) for char in ['!', '#', '$', '%', '&', '(', ')', '*', ';', '<', '=', '>', '?', '@', '[', '\', ']', '^', '_', '`', '{', '|', '}', '~']):
            return False
    return True

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'error', 'message': 'Invalid host parameter'}
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}