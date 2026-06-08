from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Function to validate the host input
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts