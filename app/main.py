from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run instead of shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)

# Function to validate the host input
def is_safe_host(host):
    # Implement validation logic here (e.g., allow only certain domain patterns, disallow shell metacharacters)
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts