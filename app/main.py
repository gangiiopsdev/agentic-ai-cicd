from fastapi import FastAPI
import subprocess
class HostSanitizer:
    def __init__(self):
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,-_. '

def is_safe_hostname(hostname: str) -> bool:
    return all(c in HostSanitizer().valid_chars for c in hostname)

class PingService:
    @staticmethod
    def ping(host: str):
        if not is_safe_hostname(host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        sanitized_host = HostSanitizer().sanitize(host)
        try:
            args = ['ping', '-c', '1', sanitized_host]  # Limit the number of pings to avoid denial of service
            result = subprocess.run(args, check=True, capture_output=True, text=True, timeout=5)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping_service.ping(host)