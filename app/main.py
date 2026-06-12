from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    async def ping(self, host: str):
        if not self.is_safe_host(host):
            return {'status': 'error', 'message': 'Invalid host'}
        # Secure implementation using shell=False and a list of arguments
        subprocess.call(['ping', '-c 4', host], shell=False)
        return {'status': 'completed'}

    def is_safe_host(self, host):
        return host in self.allowed_hosts

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping(host: str):
    return ping_service.ping(host)