from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_path = "/bin/ping" # Full path to ping executable

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output([ping_service.ping_path, host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}