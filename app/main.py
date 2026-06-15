from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed IP addresses or domain names.
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts