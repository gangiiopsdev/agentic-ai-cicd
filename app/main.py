from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):