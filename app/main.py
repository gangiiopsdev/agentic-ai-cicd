from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout,

def validate_host(host):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = PingCommand(host)
    output = command.execute()
    return {'status': 'completed', 'output': output}