from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), result.stderr.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    command = PingCommand(host)\n    stdout, stderr = await command.run()\n    return {"status": "completed", "stdout": stdout, "stderr": stderr}