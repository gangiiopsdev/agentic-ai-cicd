from fastapi import FastAPI
import subprocess
from typing import Optional
from shlex import quote
class PingService:
    def __init__(self):
        self.hosts = []

    def sanitize_input(self, input_str: str) -> str:
        return ''.join(filter(str.isalnum, input_str))

    async def ping_host(self, host: Optional[str] = None) -> dict:
        if host is None or not host.strip():
            return {'status': 'failed', 'error': 'Invalid input'}
        sanitized_host = self.sanitize_input(host)
        try:
            output = subprocess.run(['ping', '-c 1', quote(sanitized_host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: Optional[str] = None):
    return ping_service.ping_host(host)