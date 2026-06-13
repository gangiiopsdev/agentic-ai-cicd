from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Use subprocess.run instead of subprocess.call
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

class PingEndpoint:
    @app.get('/ping')
    def ping_endpoint(self, host: str):
        ping_service = PingService()
        return ping_service.ping(host)