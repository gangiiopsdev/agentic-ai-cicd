from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global_app = FastAPI()

@global_app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    response = command.execute()
    return {'status': 'completed', 'response': response}