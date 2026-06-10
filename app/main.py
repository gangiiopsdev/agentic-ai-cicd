from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in host:
        if char not in allowed_chars:
            raise ValueError("Invalid character in hostname")
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_host = escape_shell_arg(host)
    args = shlex.split(f'ping {safe_host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}