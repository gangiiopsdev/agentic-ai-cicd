from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with shell=False and argument parsing
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'stdout': result.stdout}
    else:
        raise ValueError('Host not allowed')