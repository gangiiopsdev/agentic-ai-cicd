from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            return await output.stdout.read()
        except Exception as e:
            return str(e)

global safe_ping
safe_ping = SafePing(None)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global safe_ping
    safe_ping.host = host
    result = safe_ping.ping()
    return {"status": "completed", "result": result}