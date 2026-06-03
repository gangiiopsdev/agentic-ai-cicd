from fastapi import FastAPI
import re

class PingService:
    @staticmethod
def ping(host: str):
        # Robust regex to validate the hostname
        if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
            return {'status': 'failed', 'error': 'Invalid characters in hostname'}
        try:
            result = subprocess.run(['ping', '-c', str(4), host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}
    return PingService.ping(host)