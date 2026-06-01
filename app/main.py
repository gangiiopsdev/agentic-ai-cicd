from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return run_ping(host)

def is_safe_host(host):
    # Implement logic to validate the host input
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts