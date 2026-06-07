from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.strip().replace('.', '', 3).isdigit():
            raise ValueError('Invalid host format')
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
class SafePingService:
    def __init__(self, allowed_hosts=None):
        if not allowed_hosts:
            allowed_hosts = []
        self.allowed_hosts = allowed_hosts

    def is_host_allowed(self, host: str) -> bool:
        for allowed_host in self.allowed_hosts:
            if host == allowed_host:
                return True
        return False

    def safe_ping(self, host: str):
        if self.is_host_allowed(host):
            try:
                # Validate and sanitize the host input
                if not host.strip().replace('.', '', 3).isdigit():
                    raise ValueError('Invalid host format')
                result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
                return result.stdout
            except subprocess.CalledProcessError as e:
                return str(e)
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
safe_ping_service = SafePingService(allowed_hosts=['127.0.0.1', '::1'])

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping_service.safe_ping(host)
        return {'status': 'completed', 'response': response}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}