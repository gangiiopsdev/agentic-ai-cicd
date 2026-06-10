from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Using check_output to avoid shell=True and ensure the command is safer
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return await result.communicate()
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    output, error = ping_command.execute()
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed', 'output': output.decode()}