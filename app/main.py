from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return stdout.decode(), stderr.decode()
        except Exception as e:
            return str(e), None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    stdout, stderr = command.execute()
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}