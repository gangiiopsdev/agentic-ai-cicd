from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        # Secure implementation
        args = ['ping', host]
        subprocess.call(args)

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)