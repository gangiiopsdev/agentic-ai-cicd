from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the input
        if not self.host.strip() or self.host.strip().endswith(' '):
            raise ValueError("Invalid host")
        command = ['ping', subprocess.quote(self.host)]
        return subprocess.run(command, capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        ping_command = PingCommand(host)
        result = ping_command.execute()
        return {'result': result.stdout}
    except ValueError as e:
        return {'error': str(e)}