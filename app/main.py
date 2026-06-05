from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> None:
        # Safe implementation using shlex.quote
        import shlex
        command = f'ping {shlex.quote(self.host)}'
        subprocess.call(command, shell=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(host)
    command_executor.execute()
    return {"status": "completed"}