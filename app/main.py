from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using shlex and subprocess.Popen
        args = ['ping', self.host]
        subprocess.run(args, check=True)
global ping_command
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global ping_command
    if not ping_command:
        ping_command = PingCommand(shlex.quote(host))
    ping_command.execute()
    return {'status': 'completed'}