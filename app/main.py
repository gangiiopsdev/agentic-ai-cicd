from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', self.host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    if result == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping failed"}