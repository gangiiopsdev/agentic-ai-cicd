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

global ping_command_instance

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global ping_command_instance
    if not ping_command_instance or ping_command_instance.host != host:
        ping_command_instance = PingCommand(host)

    return {'status': 'completed', 'result': ping_command_instance.execute()}