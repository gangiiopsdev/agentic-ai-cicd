from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await self._execute()
        return result

    async def _execute(self):
        command = ['ping', self.host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            raise Exception(f'Error executing ping: {error.decode()}')
        return {'status': 'completed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()