from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the host to avoid command injection
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific domains/IPs
    allowed_hosts = ['example.com']  # Replace with actual allowed hosts
    return host in allowed_hosts