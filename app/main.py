from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c.isdigit())
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping'] + shlex.split(sanitized_host), check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}