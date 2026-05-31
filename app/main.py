from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run with strict validation of host input
        if not all(c.isalnum() or c in '.-:' for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not all(c.isalnum() or c in '.-:' for c in host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return PingService.ping(host)