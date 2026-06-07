from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping_safe(host)