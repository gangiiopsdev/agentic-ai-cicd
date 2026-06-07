from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str) -> dict:
    # Secure implementation with validation and sanitization
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}, 403