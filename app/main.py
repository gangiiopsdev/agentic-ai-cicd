from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic, e.g., allow only specific domains or IPs
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts