from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    @staticmethod
    def sanitize_host(host: str) -> str:
        # Basic sanitization to avoid injection attacks
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        sanitized_host = ''.join(char for char in host if char in allowed_chars)
        return sanitized_host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}