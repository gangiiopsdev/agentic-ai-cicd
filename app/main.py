from fastapi import FastAPI
import subprocess
global_host = 'example.com' # Replace with a safe default value or use environment variables

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts