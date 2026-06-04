from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure host is sanitized before use
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host
    return True
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping(host)