from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', '-c', '1', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    command = PingCommand(host)\n    status = command.execute()\n    return {'status': 'completed', 'output': status}