from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    response = command.execute()
    return {'status': 'completed', 'output': response}