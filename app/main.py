from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', '-c', '1', self.host], check=True, text=True, capture_output=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()