from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host contains only valid characters
    return all(c.isalnum() or c in '.-[]' for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    # Use a whitelist of allowed hosts to avoid command injection
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'error': 'Host not allowed'}
    result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}