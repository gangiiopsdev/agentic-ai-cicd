from fastapi import FastAPI
import subprocess
import shlex
class InputValidator:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def validate_host(self, host: str) -> bool:
        return all(char in self.allowed_chars for char in host)

class PingService:
    def __init__(self):
        self.validator = InputValidator()

    async def ping(self, host: str) -> dict:
        if not self.validator.validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            args = ['ping'] + shlex.split(host)
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
ping_service = PingService()

@app.get('/ping/{host}')
def ping_endpoint(host: str):
    return ping_service.ping(host)