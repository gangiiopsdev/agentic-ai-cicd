from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        # Secure implementation
        if not self.is_valid_host(host):
            raise ValueError('Invalid host name')
        args = ['ping', host]
        subprocess.call(args)

    def is_valid_host(self, host: str) -> bool:
        # Add validation logic here (e.g., regex pattern matching)
        return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

global app
app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)