from fastapi import FastAPI
import subprocess
class CommandRunner:
    def __init__(self):
        self.commands = {'ping': 'ping'}

    async def run_command(self, host: str, command: str = 'ping'):
        if command in self.commands and self.is_valid_host(host):
            try:
                output = subprocess.check_output([command, host], stderr=subprocess.STDOUT, shell=False)
                return {'status': 'completed', 'output': output.decode()}
            except subprocess.CalledProcessError as e:
                return {'status': 'error', 'output': e.output.decode()}

    def is_valid_host(self, host: str) -> bool:
        # Add validation logic to ensure the host input is safe
        return True  # Placeholder for actual validation

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    runner = CommandRunner()
    return runner.run_command(host)