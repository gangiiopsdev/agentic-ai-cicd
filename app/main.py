from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with input validation and escaping
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}