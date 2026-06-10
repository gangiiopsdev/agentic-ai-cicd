from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', 'localhost']

    async def ping(self, host: str) -> dict:
        if not self.is_safe_host(host):
            return {'status': 'failed', 'error': 'Host is not allowed'}
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    def is_safe_host(self, host: str) -> bool:
        sanitized_host = ''.join(c for c in host if c.isalnum() or c in ['.', ':'])
        return sanitized_host in self.allowed_hosts

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    if not safe_ping.is_safe_host(host):
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}