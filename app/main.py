from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    async def ping(self, host: str) -> dict:
        if host not in self.allowed_hosts:
            return {'status': 'error', 'message': 'Unauthorized host'}
        args = ['ping', host]
        subprocess.call(args)
        return {'status': 'completed'}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)