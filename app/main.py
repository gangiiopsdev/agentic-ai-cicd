from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Use subprocess.run with a list to avoid shell=True and potential command injection
            result = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Create a PingCommand instance and execute the command safely
    ping_command = PingCommand(host)
    status = ping_command.execute()
    return {"status": "completed", "result": status}