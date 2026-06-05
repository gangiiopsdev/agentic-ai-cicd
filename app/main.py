from fastapi import FastAPI
import subprocess
import re
class PingService:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run with strict validation of host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Ensure the host input is safe by validating it
    if not PingService.ping(host)['status'] == 'completed':
        return {'status': 'failed', 'error': 'Invalid host'}
    return PingService.ping(host)