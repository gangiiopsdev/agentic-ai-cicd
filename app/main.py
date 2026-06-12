from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input to prevent command injection
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to ensure it only contains expected characters
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return PingService.ping(host)