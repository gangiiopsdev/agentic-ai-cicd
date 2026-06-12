from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid hostname'}
    # Sanitize input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c == '.')
    return safe_ping(safe_host)