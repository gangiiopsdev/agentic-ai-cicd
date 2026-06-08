from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host}')
    output = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}
class PingService:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/ping')
    def ping(self, host: str):
        try:
            result = safe_ping(host)
            return result
        except ValueError as e:
            return {'status': 'failed', 'error': str(e)}
ping_service = PingService()