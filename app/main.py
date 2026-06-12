from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '--count=1', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts