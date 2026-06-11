from fastapi import FastAPI
import subprocess
class CommandExecution:
    def __init__(self):
        self.commands = {
            "ping": self.ping,
        }

    async def execute_command(self, cmd, args):
        if cmd in self.commands and cmd == 'ping':  # Ensure the command is explicitly allowed
            return await self.commands[cmd](args)
        else:
            raise ValueError(f"Command {cmd} not allowed")

    async def ping(self, host: str):
        subprocess.call(["ping", subprocess.list2cmdline(args)])  # Use list2cmdline for better security
        return {"status": "completed"}

app = FastAPI()
app.command_execution = CommandExecution()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return app.command_execution.execute_command('ping', [host])