from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement a function to validate the host input
    return host.replace('.', '_').replace('-', '_').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}