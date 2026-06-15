from fastapi import FastAPI
import subprocess
class CommandRunner:
    def __init__(self, command: list):
        self.command = command

    def run(self):
        return subprocess.run(self.command, capture_output=True, text=True)

app = FastAPI()

command_runner = CommandRunner(['ping', 'host'])

@app.get("/ping")
def ping_route(host: str):
    return command_runner.run()