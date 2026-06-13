from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command):
        self.command = command

    def execute(self):
        return subprocess.run(self.command.split(), check=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    ping_instance = PingCommand(command)
    result = ping_instance.execute()
    return {"status": "completed", "output": result}