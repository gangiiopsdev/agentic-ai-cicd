from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        if not self.host or len(self.host) > 255:
            return {'status': 'error', 'output': 'Invalid host'}
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host and len(host) <= 255:
        command = PingCommand(host)
        return command.execute()
    else:
        return {'status': 'error', 'output': 'Invalid host'}