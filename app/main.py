from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        subprocess.call(['ping', self.host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    command.run()
    return {"status": "completed"}