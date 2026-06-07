from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    service = PingService()
    return service.ping(subprocess.quote(host))

# Function to validate the host input
import re
def is_valid_host(hostname: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, hostname) is not None