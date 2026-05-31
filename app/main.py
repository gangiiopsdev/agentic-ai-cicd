from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

    def execute(self):
        try:
            subprocess.call(['ping', self.host], shell=False)
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
        return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()