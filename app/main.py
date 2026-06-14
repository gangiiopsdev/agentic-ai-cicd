from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host format')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Additional validation and sanitization
    if not host.replace('.', '').isalnum():
        raise ValueError('Invalid host format')
    return run_ping(host)