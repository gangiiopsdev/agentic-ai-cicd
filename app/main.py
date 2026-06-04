from fastapi import FastAPI
import subprocess

def execute_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in '.-\' for c in host):  # Allow alphanumeric, dots, hyphens, and backslashes
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)