from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., regex match for allowed hostnames/IPs
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True