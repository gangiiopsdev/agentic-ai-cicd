from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation for security
    if not host.strip().isalnum() and not (host.strip('0123456789.-').startswith('.') or host.count('.') == 3):  # Basic validation for alphanumeric or IP address
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}