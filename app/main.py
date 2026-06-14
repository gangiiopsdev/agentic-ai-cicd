from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add valid hosts here
    return host in allowed_hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping'], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}