from fastapi import FastAPI
import subprocess
import shlex
class SafeHostChecker:
    allowed_hosts = ['example.com', 'test.com']

    @staticmethod
def is_safe_host(host):
        return host in SafeHostChecker.allowed_hosts
class PingEndpoint:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        if not SafeHostChecker.is_safe_host(host):
            raise ValueError('Unsafe host')
        args = shlex.split(f'ping {host}')
        try:
            subprocess.run(args, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        return {'status': 'completed'}
ping_endpoint = PingEndpoint().ping