from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    output = ping_command.execute()
    return {'status': 'completed', 'output': output}