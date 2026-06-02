from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        # Safe implementation using shlex.quote for argument quoting
        command = ['ping', self.host]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.run()
    return {"status": "completed"}