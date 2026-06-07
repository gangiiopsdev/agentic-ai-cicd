from fastapi import FastAPI
import subprocess
import re
class PingService:
    def ping(self, host: str):
        # Validate and sanitize input to prevent shell injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return 'Invalid hostname'
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e!r}'
global_ping_service = PingService()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return global_ping_service.ping(host)