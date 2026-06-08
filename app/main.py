from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.run(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    command = PingCommand(host)
    command.execute()

    return {"status": "completed"}