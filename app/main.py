from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = host.strip()
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    if not host or not isinstance(host, str):
        return {'status': 'invalid', 'message': 'Invalid input'}
    return ping(host)