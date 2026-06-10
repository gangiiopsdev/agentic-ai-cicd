from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            result = await asyncio.create_subprocess_exec('ping', host,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            output, _ = await result.communicate()
            return output.decode().strip()
        except Exception as e:
            return str(e)

app = FastAPI()

cp = SafePing()

@app.get("/ping")
def ping(host: str):
    return cp.ping(host)