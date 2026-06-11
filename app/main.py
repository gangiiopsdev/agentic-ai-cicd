from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_path = ['ping']

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(ping_service.ping_path + [host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}