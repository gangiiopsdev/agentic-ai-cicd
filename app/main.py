from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation using a list of arguments
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}