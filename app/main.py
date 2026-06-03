from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        # Safe implementation without shell=True
        args = ['ping', self.host]
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {"status": "invalid_host", "error": "Invalid hostname provided."}, 400
    command = PingCommand(host)
    command.run()
    return {"status": "completed"}