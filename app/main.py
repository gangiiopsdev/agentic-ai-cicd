from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()

app = FastAPI()

@app.get("/ping")
def ping(host: str):  
    if not host.isalnum():  # Basic validation to ensure the input contains only alphanumeric characters
        return {'status': 'error', 'message': 'Invalid input'}
    command = PingCommand(host)
    output, error = command.execute()
    if error:
        return {'status': 'error', 'message': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}