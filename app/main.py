from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global_host = '127.0.0.1'  # Use a fixed or sanitized host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(global_host)  # Use the fixed global host
    output = command_executor.execute()
    return {'status': 'completed', 'output': output}