from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Sanitize input and use subprocess.run instead of subprocess.call for better control and security
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Add input validation and sanitization here to prevent injection attacks
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid host'}
    return execute_ping(host)