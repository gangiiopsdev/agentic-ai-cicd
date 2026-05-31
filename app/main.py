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
            subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping_service.ping(host)