from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Using subprocess.run instead of subprocess.call and avoiding shell=True
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output = command.execute()
    return {'status': 'completed', 'output': output}