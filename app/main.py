from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    # Sanitize host input to prevent shell injection
    return ''.join(c for c in host if c.isalnum() or c == '.' or c == '-').rstrip('.-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Ensure that the host input is properly sanitized before using it with subprocess
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'error', 'output': 'Invalid host'}, 400
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}, 500