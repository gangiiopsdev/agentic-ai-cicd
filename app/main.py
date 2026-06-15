from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)