from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure host is sanitized to avoid command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return 'Invalid hostname'
    result = subprocess.run(['ping', f'-c 1 {host}'], capture_output=True, text=True)
    return result.stdout
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}