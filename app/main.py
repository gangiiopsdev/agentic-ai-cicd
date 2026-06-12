from fastapi import FastAPI
import subprocess
def safe_subprocess(command):
    if not all(c.isalnum() or c in [' ', '-'] for c in ' '.join(command)):
        raise ValueError('Invalid characters in command')
    return subprocess.call(command, shell=False)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}
    sanitized_host = ''.join(filter(str.isalnum, host))
    command = ['ping', sanitized_host]
    try:
        safe_subprocess(command)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}