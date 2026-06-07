from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        result = subprocess.run(['ping', subprocess.quote(self.host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
def ping(host: str):
    command = PingCommand(host)
    return command.execute()