from fastapi import FastAPI
import subprocess
def is_safe_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'reason': 'Invalid host'}, 400

    # Secure implementation using a safe command list with validation of the input
    subprocess.run(['ping', host], check=True)

    return {'status': 'completed'}