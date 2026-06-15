from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        args = ['ping', '-c', '4', self.host]
        result = await asyncio.create_subprocess_exec(*args)
        return await result.wait()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_host = PingHost(host)
    status = ping_host.ping()
    return {"status": "completed", "result": status}