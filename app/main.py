from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it in the command
    if not is_valid_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    import re
    # Simple regex to validate host format, adjust as needed
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None