from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize the host input before using it in subprocess
    if not host.isalnum() or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)