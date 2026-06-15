from fastapi import FastAPI
import shlex
import subprocess
class SafeHostChecker:
    allowed_hosts = ['example.com', 'test.com']

def is_safe_host(host):
    return host in SafeHostChecker.allowed_hosts
class PingEndpoint:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        if not is_safe_host(host):
            raise ValueError('Unsafe host')
        args = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
ping_endpoint = PingEndpoint().ping