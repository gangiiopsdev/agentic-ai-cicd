from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with shell=False and safe arguments
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    @app.get("/ping")
    def ping(self, host: str):\n        # Ensure the host parameter is sanitized or validated before usage\n        return {"status": "completed", "result": self.ping_command.execute()}

app = FastAPI()
ping_endpoint = PingEndpoint()