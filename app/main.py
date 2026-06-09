from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str): 
    cmd = PingCommand(host)
    output = cmd.execute()
    return {"status": "completed", "output": output}