from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed', 'output': run_ping(host)}
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts