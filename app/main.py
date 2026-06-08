from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Add input validation and consider using a safer alternative to subprocess for pinging
    sanitized_host = sanitize_input(host)
    if sanitized_host:
        try:
            result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        raise ValueError('Invalid host')