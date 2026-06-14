from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
        return result.stdout.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    ping_instance = Ping(host)
    status = ping_instance.execute()
    return {"status": status}