from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def safe_execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stderr=subprocess.STDOUT)
            return True, (await output.communicate())[0].decode()
        except subprocess.CalledProcessError as e:
            return False, e.output.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing(host)
    success, result = await safe_ping_instance.safe_execute()
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}