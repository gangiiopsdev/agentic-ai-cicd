from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', '-c', '4', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand(host='')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    output = ping_command.execute()
    return {"status": "completed", "output": output}