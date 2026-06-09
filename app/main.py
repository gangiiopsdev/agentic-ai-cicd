from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call and sanitize input
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid shell injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return execute_ping(host)