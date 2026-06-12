from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True, host
    return False, None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    is_safe, sanitized_host = safe_ping(host)
    if is_safe:
        command = ['ping', '-c', '1'] + shlex.split(sanitized_host)
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}