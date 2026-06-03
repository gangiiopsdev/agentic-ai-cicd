from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host or len(host) > 256 or any(c in host for c in [';', '&', '|', '`', '$', '(', ')', '[', ']', '{', '}', ';', '\']):
        return {'status': 'failed', 'error': 'Invalid host input'}
    return safe_ping(host)