from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Add logic to check if the host is safe (e.g., whitelist, blacklist)
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts