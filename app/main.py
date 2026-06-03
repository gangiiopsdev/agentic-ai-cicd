from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', '-c', '1', self.host]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters or patterns
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'output': result.stdout}