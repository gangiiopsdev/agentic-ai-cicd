from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate input to prevent command injection
        if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
            return {'status': 'failed', 'error': 'Invalid characters in host'}
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)