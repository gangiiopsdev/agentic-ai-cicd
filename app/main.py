from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed', 'result': safe_ping(host)}

def is_safe_host(host):
    # Implement logic to check if the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts