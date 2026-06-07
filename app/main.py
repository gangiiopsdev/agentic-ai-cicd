from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '4'] + shlex.split(self.host), stderr=subprocess.STDOUT)
            return output.decode()
        except subprocess.CalledProcessError as e:
            return e.output.decode()
class PingRouter:
    def __init__(self):
        self.ping_command = PingCommand('host')

    async def ping(self, host: str):
        if not host.isnumeric():  # Simple validation to avoid injection
            return {'error': 'Invalid input'}
        result = self.ping_command.execute()
        return {'status': 'completed', 'result': result}

app = FastAPI()
ping_router = PingRouter()

@app.get("/ping")
def ping(host: str):
    return ping_router.ping(host)