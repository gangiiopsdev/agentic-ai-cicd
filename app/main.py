from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.safe_commands = {'ping'}

    def is_safe_command(self, command):
        return command in self.safe_commands

app = FastAPI()
ping_command_instance = PingCommand()

@app.get("/ping")
def ping(host: str):
    if ping_command_instance.is_safe_command('ping'):
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Unsafe command"}