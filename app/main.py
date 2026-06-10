from fastapi import FastAPI
import re
import shlex
import subprocess
class PingService:
    def ping(self, host: str) -> dict:
        if not self.validate_host(host):
            return {'status': 'error', 'message': 'Invalid input'}
        command = ['ping', host]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

    def validate_host(self, host: str) -> bool:
        # Example validation logic, replace with actual validation
        return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None
global ping_service
ping_service = PingService()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return ping_service.ping(host)