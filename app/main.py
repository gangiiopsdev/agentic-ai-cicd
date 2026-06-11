from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class SafePingService:
    def __init__(self):
        self.valid_hosts = ['example.com']  # Define a whitelist of allowed hosts

    def ping(self, host: str):
        if host not in self.valid_hosts:
            raise ValueError('Invalid host')
        return safe_ping(host)

app = FastAPI()
safe_ping_service = SafePingService()

@app.get("/ping")
def ping(host: str):
    result = safe_ping_service.ping(host)
    return {"status": "completed", "result": result}