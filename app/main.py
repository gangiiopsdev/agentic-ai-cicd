from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation with argument validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}