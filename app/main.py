from fastapi import FastAPI
import subprocess
global safe_hosts = ['example.com', 'localhost']  # Define allowed hosts
def is_safe_host(host):
    return host in safe_hosts

def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)