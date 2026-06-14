from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        return await asyncio.create_subprocess_exec('ping', f'\"{self.host}\"', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService(host)
    result = await service.ping()
    if result == 0:
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}