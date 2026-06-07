from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize the host input
        sanitized_host = ''.join(e for e in host if e.isalnum())
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}

app = FastAPI()

@app.get('/ping')
def ping_handler(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid hostname', 'status': 'failed'}
    sanitized_host = ''.join(e for e in host if e.isalnum())
    return ping(sanitized_host)