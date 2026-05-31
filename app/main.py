from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    args = ['ping', sanitized_host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent command injection
        return {'status': 'error', 'message': 'Invalid input'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}