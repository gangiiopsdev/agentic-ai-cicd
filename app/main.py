from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize the input to prevent shell injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    result = PingService.ping(host)
    return {'status': 'completed', 'stdout': result.stdout}