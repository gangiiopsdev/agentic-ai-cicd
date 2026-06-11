from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status = command.execute()
    return {"status": "completed", "output": status}