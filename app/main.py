from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> None:
        args = ['ping', self.host]
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()