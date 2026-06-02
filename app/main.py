from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', '-c', '1', shlex.quote(self.host)]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters or patterns
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'output': result.stdout}