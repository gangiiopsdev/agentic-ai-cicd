from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input
    if host.strip() != host or host.startswith('-'):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}