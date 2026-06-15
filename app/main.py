from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to prevent potential injection attacks
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        # Safe implementation using subprocess.run with shell=False
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., regex to match allowed hostnames/IPs
    return host.isdigit() or host.count('.') == 3