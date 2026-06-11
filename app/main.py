from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts