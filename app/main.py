from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        return await subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)
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
    result = await ping_command.run()
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}