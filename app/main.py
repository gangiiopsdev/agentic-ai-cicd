from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', self.host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status = command.execute()
    return {"status": "completed", "return_code": status}