from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> dict:
        try:
            args = shlex.split(f'ping -c 1 {self.host}')
            output = subprocess.check_output(args, timeout=5, stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()