from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            result = subprocess.call(['ping', host])
            return {'status': 'completed'}
        else:
            return {'error': 'Unauthorized host'}, 403

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)