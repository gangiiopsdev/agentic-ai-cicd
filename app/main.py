from fastapi import FastAPI
import subprocess
def ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}