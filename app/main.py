from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}