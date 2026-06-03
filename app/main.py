from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return safe_ping(host)
def validate_host(host):
    # Implement a validation logic here, e.g., allow only specific domains or IP addresses
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts