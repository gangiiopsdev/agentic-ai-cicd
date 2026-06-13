from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using list for args and avoiding shell execution
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    command.execute()
    return {"status": "completed"}