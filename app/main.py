from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate host input to prevent injection
        if not all(c.isalnum() or c in '.-' for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}