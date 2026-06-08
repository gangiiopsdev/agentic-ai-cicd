from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        return await asyncio.create_subprocess_exec('ping', self.host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    result = safe_ping.ping()
    return {'status': 'completed'}