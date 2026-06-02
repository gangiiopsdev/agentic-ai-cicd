from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    def ping(self, host: str):
        # Using a safe method to execute the command
        return {'status': 'completed', 'output': self.ping_command.execute()}

app = FastAPI()

global_ping_endpoint = PingEndpoint()

@app.get("/ping")
def ping(host: str):
    return global_ping_endpoint.ping(host)