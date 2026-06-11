from fastapi import FastAPI
import subprocess
import re
class PingService:
    def ping(self, host: str):
        # Validate the host input to ensure it is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)