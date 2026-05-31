from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        return {'status': 'error', 'error': 'Invalid host'}
    return ping(host)