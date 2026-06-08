from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.local']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        return {'status': safe_ping(host)}
    else:
        return {'error': 'Host not allowed'}