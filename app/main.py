from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.replace('.', '', 3).isdigit():
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', f'-c 4 {host}'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}