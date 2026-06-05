from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.Popen for a safer alternative
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'output': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}