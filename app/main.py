from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the host input
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}
def is_valid_host(host: str) -> bool:
    # Implement validation logic for the host
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(c in valid_chars for c in host)