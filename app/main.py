from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    # Simple sanitization: only allow alphanumeric characters and hyphens
    return ''.join(c for c in value if c.isalnum() or c == '-').strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    # Use shell=False to prevent command injection and avoid using shell=True unless absolutely necessary
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}