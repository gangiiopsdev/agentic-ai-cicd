from fastapi import FastAPI
import subprocess
class HostSanitizer:
    def __init__(self):
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,-_. '
def is_valid_host(host: str) -> bool:
    return all(c in HostSanitizer().valid_chars for c in host)
class PingService:
    @staticmethod
def ping(host: str):
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            args = ['ping', '--', host]
            # Sanitize the input before passing it to subprocess
            sanitized_args = [arg.encode('utf-8').decode('unicode_escape') for arg in args]
            subprocess.check_output(sanitized_args, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping_service.ping(host)