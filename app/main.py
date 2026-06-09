from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1'] + shlex.split(self.sanitize_host(host)), stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

    def sanitize_host(self, host: str) -> str:
        # Add logic to sanitize the input host
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        sanitized_host = ''.join(char for char in host if char in allowed_chars)
        return sanitized_host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)