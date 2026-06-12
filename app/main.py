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
        # Validate the host input to ensure it's a valid hostname or IP address
        import re
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host input'}
        result = subprocess.run(ping_service.ping_path + [host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}