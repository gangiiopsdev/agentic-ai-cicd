from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or '.' in host:
        return False
    return True

def safe_subprocess(command, *args):
    # Ensure the command and arguments are properly quoted and escaped
    full_command = [shlex.quote(cmd) for cmd in command]
    full_command.extend(shlex.quote(arg) for arg in args)
    result = subprocess.run(full_command, capture_output=True, text=True, check=True)
    return result.stdout

def validate_and_safe_subprocess(command, *args):
    # Validate the command and arguments before executing
    if not all(arg.isalnum() or '.' in arg for arg in args):  # Simplified validation
        raise ValueError('Invalid input')
    return safe_subprocess(command, *args)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        result = validate_and_safe_subprocess(['ping', host], shell=False)
        return {'status': 'completed', 'output': result}
    else:
        return {'error': 'Invalid host'}