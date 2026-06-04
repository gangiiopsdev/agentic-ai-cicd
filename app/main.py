from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> None:
        args = ['ping', *shlex.split(self.host)]
        subprocess.call(args)
class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self, host: str):
        self.ping_command.execute()

app = FastAPI()
ping_endpoint = PingEndpoint()
@app.get("/ping")
def ping(host: str):