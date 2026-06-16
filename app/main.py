from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and arguments
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
def validate_host(host: str) -> bool:
    if not host.isalnum() and '-' in host:
        raise ValueError('Invalid host parameter')
    return True
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate or sanitize input
    try:
        validate_host(host)
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}