from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    ping_cmd = PingCommand(command)
    return ping_cmd.execute()