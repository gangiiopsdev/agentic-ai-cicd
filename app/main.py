from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        # Secure implementation
        try:
            result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not host.strip() or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid host'}
    # Sanitize input to ensure it does not contain unexpected characters
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in '.-')
    return PingService.ping(sanitized_host)