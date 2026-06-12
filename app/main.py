from fastapi import FastAPI
import subprocess
class CommandExecution:
    def __init__(self):
        self.safe_commands = ['ping']

    def execute(self, command, *args):
        if command in self.safe_commands:
            subprocess.call([command] + list(args))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_executor = CommandExecution()
    command_executor.execute('ping', host)
    return {"status": "completed"}