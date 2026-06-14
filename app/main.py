from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return str(e)
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(subprocess.quote(host))
    output = command_executor.execute()
    return {"status": "completed", "output": output}