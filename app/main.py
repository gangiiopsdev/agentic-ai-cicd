from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.host = None

    def set_host(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    def ping(self, host: str):
        self.ping_command.set_host(host)
        return {'status': 'completed', 'output': self.ping_command.execute()}

app = FastAPI()

dep = PingEndpoint()

@app.get("/ping")
def ping(host: str):
    return dep.ping(host)