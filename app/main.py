from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def validate_host(self):
        allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
        if self.host not in allowed_hosts:
            raise ValueError('Host is not allowed')

    async def execute(self):
        await self.validate_host()
        args = ['ping', self.host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'output': result.stdout}