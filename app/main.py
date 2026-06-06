from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input
        if host.startswith('.') or ' ' in host:
            return {'status': 'Invalid host'}
        try:
            subprocess.run(['ping', host], check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {'status': f'Ping failed: {e}'}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)