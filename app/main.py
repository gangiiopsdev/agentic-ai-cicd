from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use the absolute path to avoid shell injection risks and validate host
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        output = subprocess.run(['/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def is_valid_host(host: str) -> bool:
    valid_hosts = ['example.com']  # Define a whitelist of allowed hosts
    return host in valid_hosts
class SafePingService:
    def __init__(self):
        self.valid_hosts = valid_hosts
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    return safe_ping(host)
app = FastAPI()
safe_ping_service = SafePingService()

@app.get("/ping")
def ping_api(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}