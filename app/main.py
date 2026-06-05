from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global ping
@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status = command.execute()
    return {"status": "completed", "output": status}