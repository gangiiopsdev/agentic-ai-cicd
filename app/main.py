from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        return subprocess.call(['ping', self.host])

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    command = PingCommand(host)
    return {'result': command.run()}