from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        # Validate host to ensure it's a safe and expected value
        if not validate_host(host):
            return {'error': 'Invalid host'}
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

# Define a function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific domain names or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts