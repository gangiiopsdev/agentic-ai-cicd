from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        try:
            output = await self.ping_host()
            return {"status": "completed", "output": output}
        except Exception as e:
            return {"status": "failed", "error": str(e)}

    async def ping_host(self):
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            raise Exception(result.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService(host)
    return ping_service.ping()