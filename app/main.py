from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():  # Basic validation
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    if not os.path.exists(f'/bin/ping') or not os.access(f'/bin/ping', os.X_OK):
        return {'status': 'error', 'message': 'Ping command not available'}
    # Sanitize input
    sanitized_host = ''.join(c for c in host if c.isalnum())
    result = subprocess.run(['/bin/ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}