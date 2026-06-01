from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

def is_safe_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping_endpoint(host: str):
    if is_safe_host(host):
        return ping(host)
    else:
        return {'error': 'Host not allowed'}