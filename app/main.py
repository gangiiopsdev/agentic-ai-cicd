from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': output.stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate user input to prevent injection attacks
    if not self.is_valid_host(host):
        raise ValueError("Invalid host name")
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return result

@PingCommand.classmethod
def is_valid_host(cls, host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True