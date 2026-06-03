from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in host)

def validate_host(host: str):
    # Add validation logic here, e.g., whitelist of allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    escaped_host = escape_host(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}