from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        try:
            args = shlex.split(f'ping {self.host}')
            subprocess.call(args)
            return {"status": "completed"}
        except Exception as e:
            return {"error": str(e), "status": "failed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.run()