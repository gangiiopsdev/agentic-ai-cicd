from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

global_result = safe_ping(host)
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        global_result = safe_ping(host)
        return {'status': 'completed', 'result': global_result}
    except ValueError as e:
        return {'error': str(e)}