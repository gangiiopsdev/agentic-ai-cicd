from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(filter(lambda x: x in allowed_chars, host))
    return sanitized_host
class SecurePing:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/ping')
    def ping(self, host: str):
        sanitized_host = sanitize_host(host)
        args = shlex.split(f'ping {sanitized_host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
secure_ping = SecurePing()