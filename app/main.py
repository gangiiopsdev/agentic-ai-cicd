from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return safe_ping(host)

# Function to check if the host is safe (e.g., whitelist of allowed hosts)
def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts