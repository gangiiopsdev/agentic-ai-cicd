from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {shlex.quote(sanitized_host)}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}