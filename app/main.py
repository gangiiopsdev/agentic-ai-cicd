from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if '/' not in host and '\' not in host and ':' not in host:
        ping_service = PingService()
        return ping_service.ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}