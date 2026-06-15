from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def __init__(self):
        self.valid_hosts = ['example.com', 'localhost']

    async def ping(self, host: str):
        if host in self.valid_hosts:
            args = ['ping', host]
            result = subprocess.run(args, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'invalid_host'}

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping(host: str):
    return ping_service.ping(host)