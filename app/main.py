from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = subprocess.quote(host)

    def run(self):
        return subprocess.run(['ping', '-c', '1', self.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
global ping_command
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    if not ping_command:
        ping_command = PingCommand(host)
    result = ping_command.run()
    return {"status": "completed", "stdout": result.stdout.decode('utf-8'), "stderr": result.stderr.decode('utf-8')}