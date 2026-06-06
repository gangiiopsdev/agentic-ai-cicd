from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    valid_hosts = ['192.168.0.0/16', '10.0.0.0/8']  # Example of more specific validation
    if not any(ip_range in host for ip_range in valid_hosts):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        output = subprocess.run(['ping', '-c', str(4), host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}