from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], capture_output=True, text=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {'status': 'completed', 'output': result.stdout}