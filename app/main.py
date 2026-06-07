from fastapi import FastAPI
import subprocess
def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', '--', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}