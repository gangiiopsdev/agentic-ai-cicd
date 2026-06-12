from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation without shell=True
        try:
            subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'Pinging successful'}
        except subprocess.CalledProcessError as e:
            return {'status': 'Ping failed with error: ' + str(e)}
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):  # Basic validation
        return {'status': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()