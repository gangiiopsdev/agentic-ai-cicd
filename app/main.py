from fastapi import FastAPI
import re
import subprocess
def ping(host: str):
    # Secure implementation with argument validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed', 'result': result.stdout}