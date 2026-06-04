from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        # Use subprocess.run() instead of subprocess.call()
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    # Ensure proper input validation and sanitization
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    return run_ping(host)