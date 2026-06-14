from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input by escaping special characters
    import shlex
    host = shlex.quote(host)
    if host in ['localhost', '127.0.0.1']:
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host for ping')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host for ping')
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}