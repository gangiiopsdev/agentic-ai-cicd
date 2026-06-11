from fastapi import FastAPI
import subprocess
from shlex import quote

class PingCommand:
    def __init__(self, host):
        self.host = quote(host)

    def execute(self):
        args = ['ping', self.host]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr}'
global ping_command
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global ping_command
    if not ping_command:
        ping_command = PingCommand(host)
    return ping_command.execute()