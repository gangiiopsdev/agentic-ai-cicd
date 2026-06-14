from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your list of allowed hosts
    return host in allowed_hosts
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)