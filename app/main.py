from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add validation logic for host here, e.g., whitelist allowed hosts
    return host in ['example.com', 'test.com']

@app.get('/ping')
def ping(host: str):  # Ensure that the host input is properly sanitized before using it with subprocess
    if not is_valid_host(host):
        return {'status': 'error', 'output': 'Invalid host'}, 400
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}, 500