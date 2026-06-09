from fastapi import FastAPI
import subprocess
import socket
def safe_ping(host: str):
    # Sanitize input to prevent injection attacks
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'invalid_host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return safe_ping(host)