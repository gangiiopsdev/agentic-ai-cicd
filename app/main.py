from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        # Secure implementation using subprocess.run with full executable path
        result = subprocess.run(['/bin/ping', self.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

def ping(host: str):
    command = PingCommand(host)
    return command.run()