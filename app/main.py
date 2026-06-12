from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return {'status': 'completed', 'output': command.execute()}