from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args)
        return {'status': 'completed'}
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)