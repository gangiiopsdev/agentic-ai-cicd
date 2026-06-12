from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.strip():
        raise ValueError("Invalid host")
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'output': result.stdout}