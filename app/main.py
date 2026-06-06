from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate host input to ensure it does not contain malicious commands
    if not host.isalnum() or '.' not in host:
        return {'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'output': e.output}