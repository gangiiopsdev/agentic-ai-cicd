from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    # Use a whitelist of allowed hosts or perform additional validation before running the command.
    if host in ['allowed_host1', 'allowed_host2']:
        return run_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}