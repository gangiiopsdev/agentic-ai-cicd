from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    return {'status': 'completed', 'output': ping_command.execute()}