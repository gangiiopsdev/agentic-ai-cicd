from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command_line(args):
    return [shlex.quote(arg) for arg in args]

def sanitize_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

def validate_host(host: str):
    # Add additional validation logic here, e.g., checking for blacklisted hostnames
    pass

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not validate_host(sanitized_host):  # Ensure validation passes
        return {'status': 'error', 'message': 'Invalid host'}
    command = escape_command_line(['ping', '-c', '1', sanitized_host])
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}