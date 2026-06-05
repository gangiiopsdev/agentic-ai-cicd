from fastapi import FastAPI
import subprocess
import shlex
def safe_command(command_parts):
    for part in command_parts:
        if "&" in part or ";" in part or "|" in part:
            raise ValueError("Unsafe characters detected in command")

class CommandRunner:
    def __init__(self, command_parts):
        safe_command(command_parts)
        self.command_parts = command_parts

    def run(self, user_input):
        result = subprocess.run(self.command_parts + shlex.split(user_input), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
global_command_runner = CommandRunner(['ping'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return global_command_runner.run(host)