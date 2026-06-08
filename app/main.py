from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Validate input before using it in the PingCommand constructor
    if not host.isnumeric():  # Example validation logic, adjust as needed
        return {'error': 'Invalid host'}, 400
    ping_command = PingCommand(host)
    ping_command.execute()