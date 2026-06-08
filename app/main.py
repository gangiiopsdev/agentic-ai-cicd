from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        if not self.host.isdigit():
            return 'Invalid input'
        command = ['ping', '-c', '1'] + shlex.split(self.host)
        return subprocess.run(command, capture_output=True, text=True)
global_ping_command = PingCommand('example.com')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping():
    result = global_ping_command.execute()
    return {"status": "completed", "output": result.stdout}