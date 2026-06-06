from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run without shell=True
        args = ['ping', '-c', '1', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global ping_command
    if not host or len(host) > 255:
        return {"status": "error", "message": "Invalid host input"}
    ping_command.host = host
    output = ping_command.execute()
    return {"status": "completed", "output": output}