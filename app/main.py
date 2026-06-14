from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    # Safe implementation
    command = PingCommand(host)
    output = command.run()
    return {'status': 'completed', 'output': output}