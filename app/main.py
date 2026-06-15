from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run with shell=False
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand(None)

    @app.get("/ping")
    def ping(self, host: str):
        self.ping_command.host = host
        return {'status': 'completed', 'output': self.ping_command.execute()}