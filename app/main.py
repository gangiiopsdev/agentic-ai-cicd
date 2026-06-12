from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate and sanitize host input
        allowed_hosts = ['example.com', 'test.example.com']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}