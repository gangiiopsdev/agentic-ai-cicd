from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await self.run_command()
        return result

    async def run_command(self):
        try:
            process = await asyncio.create_subprocess_exec('ping', self.host,
                                                           stdout=subprocess.PIPE,
                                                           stderr=subprocess.PIPE)
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                return {'error': stderr.decode()}
            else:
                return {'stdout': stdout.decode()}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return result