from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Unauthorized ping request')
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': ping_service.safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}