from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate and sanitize host input to prevent command injection
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return PingService.ping(host)