from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command_parts = ['ping', *shlex.split(self.host)]
        try:
            result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Command execution failed: {e}')

    def is_safe_command(self, command: str) -> bool:
        allowed_commands = ['ping']
        return any(cmd in command for cmd in allowed_commands)
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cmd = PingCommand(host)
    result = cmd.execute()
    return {'status': 'completed', 'output': result}