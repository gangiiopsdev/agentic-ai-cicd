from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() and not any(c in host for c in '.-'):  # Basic validation, improve as needed
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)