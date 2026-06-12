from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()