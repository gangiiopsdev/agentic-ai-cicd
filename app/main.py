from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Host is not allowed')
    return safe_ping(host)

def is_safe_host(host: str):
    # Implement a list of allowed hosts or patterns
    allowed_hosts = ['127.0.0.1', 'localhost']
    for allowed_host in allowed_hosts:
        if host == allowed_host or host.startswith(allowed_host + '.'):  # Add additional checks as needed
            return True
    return False