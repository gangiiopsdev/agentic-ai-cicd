from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return f'ping {self.host}'

global_ping_command = PingCommand('example.com')

app = FastAPI()

@app.get("/ping")
def ping():
    result = global_ping_command.execute()
    # Execute the ping command safely without shell=True
    subprocess.call(result, shell=False)
    return {"status": "completed"}