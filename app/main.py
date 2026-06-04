from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate input to prevent injection
        valid_hosts = ['8.8.8.8', '127.0.0.1']  # Example list of allowed hosts
        if host not in valid_hosts:
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'error': str(e)}

# Additional security controls
import os
def is_safe_path(path):
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(os.getcwd()):
        raise ValueError('Unsafe path')