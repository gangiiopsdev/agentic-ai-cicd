from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host to ensure it's safe to ping
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    try:
        output = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def is_safe_host(host: str) -> bool:
    # Implement your validation logic here, e.g., allow only certain IP ranges or domain names.
    allowed_hosts = ['127.0.0.1', '::1']  # Example
    return host in allowed_hosts