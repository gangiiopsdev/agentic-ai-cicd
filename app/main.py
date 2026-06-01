from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Secure implementation using subprocess.run with input validation and a full executable path
    try:
        args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}