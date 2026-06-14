from fastapi import FastAPI
import re
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate input
        if not host.strip():
            raise ValueError('Invalid host')
        # Sanitize input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host')
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.ping(host)