from fastapi import FastAPI
class SafePing:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        return await asyncio.create_subprocess_exec('ping', self.host, shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    result = await safe_ping.ping()
    return {'status': 'completed'}