from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)