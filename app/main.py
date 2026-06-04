from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Using subprocess.Popen instead of subprocess.call
        args = ['ping', self.host]
        process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()