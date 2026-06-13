from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'output': result.stdout}