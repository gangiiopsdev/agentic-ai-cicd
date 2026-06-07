from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(c for c in input_str if c in allowed_chars)
app = FastAPI()
@app.get('/ping')
def ping(host: str):    sanitized_host = sanitize_input(host)    try:
        output = subprocess.check_output(shlex.split(f'ping {shlex.quote(sanitized_host)}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output}