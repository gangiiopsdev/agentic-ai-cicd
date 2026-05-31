from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric() or len(host.split('.')) != 4:
        return {'status': 'error', 'message': 'Invalid IP address'}
    command = PingCommand(host)
    output = command.execute()
    return {'status': 'completed', 'output': output}