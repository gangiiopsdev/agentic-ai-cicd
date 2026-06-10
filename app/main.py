from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)