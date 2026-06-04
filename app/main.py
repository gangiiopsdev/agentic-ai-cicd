from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', self.host]
        try:
            result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {"status": "error", "message": "Invalid host"}
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {"status": "completed", "result": result}