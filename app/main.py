from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run and args
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output = command.execute()
    return {"status": "completed", "output": output}