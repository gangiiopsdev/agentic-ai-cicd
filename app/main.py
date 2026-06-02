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
    # Add additional validation logic here, e.g., checking for blacklisted hostnames
    pass

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_host(host)
    validate_host(sanitized_host)
    command = escape_command_line(['ping', '-c', '1', sanitized_host])
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}