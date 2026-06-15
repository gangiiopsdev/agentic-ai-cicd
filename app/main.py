from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        allowed_hosts = ["example.com", "127.0.0.1"]
        if self.host in allowed_hosts:
            subprocess.call(['ping', self.host])
        else:
            raise ValueError("Host not allowed")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    try:
        command = PingCommand(host)
        command.execute()
        return {"status": "completed"}
    except ValueError as e:
        return {"status": "denied", "error": str(e)}