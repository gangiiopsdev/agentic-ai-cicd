from fastapi import FastAPI
import subprocess
class CommandRunner:
    def __init__(self):
        self.commands = {'ping': 'ping'}

    async def run_command(self, host: str, command: str = 'ping'):
        if command in self.commands and host:
            try:
                output = subprocess.check_output([command, host], stderr=subprocess.STDOUT, shell=False)
                return {'status': 'completed', 'output': output.decode()}
            except subprocess.CalledProcessError as e:
                return {'status': 'error', 'output': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    runner = CommandRunner()
    return runner.run_command(host)