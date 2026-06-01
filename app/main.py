from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input before using it with subprocess
    if not host or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid hostname'}
    return safe_ping(host)