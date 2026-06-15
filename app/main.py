from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    def validate_host(self, host):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')

    async def ping(self, host: str):
        if await self.validate_host(host):
            command = ['ping', host]
            result = subprocess.run(command, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
executor = CommandExecutor()

@app.get('/ping')
def ping_endpoint(host: str):
    return executor.ping(host)