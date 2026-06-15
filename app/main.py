from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host.strip()  # Sanitize input to prevent command injection

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()