from fastapi import FastAPI
import subprocess
global safe_hosts
safe_hosts = ['127.0.0.1', '::1']  # List of allowed hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Host not allowed'}
    # Safer implementation using subprocess.run with shell=False and proper argument passing
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def is_safe_host(host):
    global safe_hosts
    return host in safe_hosts