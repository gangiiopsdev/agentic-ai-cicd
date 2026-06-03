from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    # Basic validation: Allow only alphanumeric characters and hyphens
    if all(c.isalnum() or c == '-' for c in host) and len(host) <= 64:
        return host
    raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), check=True, timeout=5, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}