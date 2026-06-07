from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    return ''.join(c for c in host if c.isalnum() and c.isdigit())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['192.168.0.1', '10.0.0.1']  # Example whitelist
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Unauthorized host'}
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(sanitized_host)], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}