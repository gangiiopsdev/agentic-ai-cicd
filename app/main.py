from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host
        self.command = ["ping", self.host]

    def execute(self) -> dict:
        result = subprocess.run(self.command, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}

global ping_command_instance

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global ping_command_instance
    if not ping_command_instance:
        ping_command_instance = PingCommand(host)
    return ping_command_instance.execute()