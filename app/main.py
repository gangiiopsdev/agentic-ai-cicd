from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Secure implementation using subprocess.run with args parameter
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_', '!'] for c in host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)