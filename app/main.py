from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            subprocess.run(['ping', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    return PingService.ping(host)