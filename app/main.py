from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        allowed_hosts = ['example.com', 'test.example.com']
        if self.host not in allowed_hosts:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {shlex.quote(self.host)}')
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        command = PingCommand(host)
        return await command.execute()
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as e:
        return {'error': str(e)}