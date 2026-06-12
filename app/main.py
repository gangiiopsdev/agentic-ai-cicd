from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run with shell=False and list of arguments
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Add validation to ensure host is alphanumeric
        return {"status": "error", "message": "Invalid input"}
    command = PingCommand(host)
    output = command.execute()
    return {"status": "completed", "output": output}