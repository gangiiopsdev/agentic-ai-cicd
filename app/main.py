from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it's a safe target for pinging
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]
    # Use subprocess.run instead of subprocess.call and check the return code
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}

# Function to validate the host input
def is_safe_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only certain IP addresses or domain names
    allowed_hosts = ['example.com', '127.0.0.1']  # Example list
    return host in allowed_hosts