from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use the absolute path to avoid shell injection risks
        output = subprocess.run(['/bin/ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
class SafePingService:
    def __init__(self):
        self.valid_hosts = ['example.com']  # Define a whitelist of allowed hosts

def ping(host: str):
    if host not in safe_ping_service.valid_hosts:
        raise ValueError('Invalid host')
    return safe_ping(host)

app = FastAPI()
safe_ping_service = SafePingService()

@app.get("/ping")
def ping_api(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}