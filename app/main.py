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

global ping_command
global app
app = FastAPI()
ping_command = PingCommand(host='127.0.0.1')

@app.get("/ping")
def ping():
    return {'status': 'completed', 'output': ping_command.execute()}