from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host to ensure it's a safe ping target
    if not safe_host_check(host):
        return {'status': 'error', 'output': 'Unsafe host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
def safe_host_check(host: str) -> bool:
    # Add logic to validate the host
    allowed_hosts = ['example.com']
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)