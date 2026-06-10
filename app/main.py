from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        try:
            # Validate and sanitize input
            if not host.replace('.', '').isnumeric() or len(host.split('.')) != 4:
                raise ValueError('Invalid host format')
            subprocess.run(['ping', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService.safe_ping(host)