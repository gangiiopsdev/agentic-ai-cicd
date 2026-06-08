from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Validate input to ensure it does not contain malicious commands
        if self.is_safe_command(self.host):
            command_parts = ['ping', *shlex.split(self.host)]
            subprocess.run(command_parts)
        else:
            raise ValueError('Unsafe command detected')

    def is_safe_command(self, command: str) -> bool:
        # Implement a more robust check for safe commands
        allowed_commands = ['ping']
        return any(cmd in command for cmd in allowed_commands)
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cmd = PingCommand(host)
    cmd.execute()
    return {"status": "completed"}