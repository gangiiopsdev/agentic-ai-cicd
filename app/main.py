from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'failed', 'output': 'Invalid host input'}
    # Sanitize the host input to prevent command injection
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}