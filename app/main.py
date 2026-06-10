from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
global_ping_command = PingCommand('')

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    global_ping_command.host = host
    return global_ping_command.execute()