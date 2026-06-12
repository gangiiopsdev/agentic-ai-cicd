from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
def is_safe_host(host):
    # Define a whitelist of allowed hosts or use a more sophisticated validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts