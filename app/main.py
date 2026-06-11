from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

ping_service = PingService()