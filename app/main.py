from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    allowed_hosts = ['google.com', 'example.com']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)