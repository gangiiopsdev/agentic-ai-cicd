from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation without shell=True
        if not self.host.isdigit():
            return 'Invalid input'
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    response = ping_command.execute()
    return {"status": "completed", "output": response}