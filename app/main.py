from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid host")
    return 'ping', host.strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command, sanitized_host = sanitize_host(host)
    result = subprocess.run(command + [sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}