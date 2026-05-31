from fastapi import FastAPI
import subprocess
class HostSanitizer:
    def __init__(self):
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,-_. '

    def sanitize(self, host: str) -> str:
        return ''.join(c for c in host if c in self.valid_chars)
class PingService:
    @staticmethod
def ping(host: str):
        sanitized_host = HostSanitizer().sanitize(host)
        # Validate and sanitize the host input
        if not all(c in HostSanitizer().valid_chars for c in sanitized_host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            args = ['ping', sanitized_host]
            subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping_service.ping(host)