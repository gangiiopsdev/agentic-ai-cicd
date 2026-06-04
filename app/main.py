from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', self.host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return {'error': 'Invalid host'}, 400
    ping_command = PingCommand(host)
    status = ping_command.execute()
    return {"status": "completed", "exit_code": status}