from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command_line(args):
    return [shlex.quote(arg) for arg in args]

def sanitize_host(host: str):
    # Define allowed characters and remove any disallowed ones
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

def validate_host(host: str):
    # Define allowed characters and remove any disallowed ones
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host parameter')
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_host(host)
    command = escape_command_line(['ping', '-c', '1', sanitized_host])
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}