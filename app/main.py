from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic to ensure the host is safe
    # Example: only allow ping to specific IP addresses or ranges
    allowed_hosts = ['192.168.1.0/24', '10.0.0.1']
    for allowed_host in allowed_hosts:
        if ipaddress.ip_address(host) in ipaddress.ip_network(allowed_host):
            return True
    return False