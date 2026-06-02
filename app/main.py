from fastapi import FastAPI
import re

class PingService:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run with validation
        if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
            if result.returncode != 0:
                return {'status': 'failed', 'error': str(result.stderr)}
            else:
                return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)