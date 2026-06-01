from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        await asyncio.create_subprocess_exec(*args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping(host)
    await ping_instance.execute()
    return {"status": "completed"}