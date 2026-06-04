from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = shlex.quote(host)

    def execute(self):
        command = ['ping', self.host]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'output': result.stdout}