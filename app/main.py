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
    subprocess.run(args, check=True)
    return {'status': 'completed'}