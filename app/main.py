from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run with shell=False and proper argument handling
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    output = ping_command.execute()
    return {"status": "completed", "output": output}