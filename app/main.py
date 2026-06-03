from fastapi import FastAPI
import subprocess
import shlex

class CommandRunner:
    def __init__(self, command_parts):
        self.command_parts = command_parts

    def run(self):
        result = subprocess.run(self.command_parts, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

global_command_runner = CommandRunner(['ping'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = global_command_runner.command_parts + shlex.split(host)
    return global_command_runner.run()