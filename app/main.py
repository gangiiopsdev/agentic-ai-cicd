from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}