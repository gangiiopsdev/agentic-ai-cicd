from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    command.execute()
    return {"status": "completed"}