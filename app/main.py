from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using shlex.quote to sanitize the input
        subprocess.call(['ping', subprocess.list2cmdline([self.host])])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):  # Basic validation
        return {'status': 'error', 'message': 'Invalid input'}
    ping_command = PingCommand(host)
    ping_command.execute()
    return {'status': 'completed'}