from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)

# Define a function to validate the host input
def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., check if the host is on a whitelist
    valid_hosts = ['example.com', 'test.com']
    return host in valid_hosts