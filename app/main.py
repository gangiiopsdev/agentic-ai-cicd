from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'response': 'Invalid host'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}

def validate_host(host):
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts