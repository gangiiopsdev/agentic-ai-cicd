from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        return True, host
    return False, None

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Validate and sanitize input
    is_safe, sanitized_host = safe_ping(host)
    if is_safe:
        result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}

# Add input validation and sanitization here to mitigate the risk.