from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Basic validation: allow only alphanumeric characters and hyphens
    return host.replace('-', '').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid hostname")

    # Use subprocess.run instead of subprocess.call for better control and error handling
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    else:
        return {'status': 'completed'}