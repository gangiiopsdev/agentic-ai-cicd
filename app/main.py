from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'output': result.stdout}