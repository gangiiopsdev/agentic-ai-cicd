from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def run_ping(host):
    try:
        # Use subprocess.Popen for better control and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to avoid injection attacks
    if not host or not os.path.basename(host).isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return run_ping(host)