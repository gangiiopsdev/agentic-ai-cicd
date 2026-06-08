from fastapi import FastAPI
import subprocess
import shlex
def sanitize_hostname(hostname):
    return ''.join(c for c in hostname if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_hostname(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid hostname'}
    command = ['ping', '-c', '1', sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}