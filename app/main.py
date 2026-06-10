from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts

    def validate_host(self, host):
        if host in self.allowed_hosts:
            return True
        else:
            raise ValueError('Invalid host')

    async def ping(self, host: str):
        try:
            self.validate_host(host)
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except (subprocess.CalledProcessError, ValueError) as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)