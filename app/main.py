from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Implement sanitization logic here, e.g., allow only specific host formats
    if not host.isalnum():  # Example simple check
        raise ValueError('Invalid hostname')
    return host

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}