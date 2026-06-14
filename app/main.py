from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingCommand:
    def __init__(self, host):
        self.host = host

    @validator('host', pre=True)
    def validate_host(cls, v):
        global_host_whitelist = {'8.8.8.8', '127.0.0.1'}
        if v not in global_host_whitelist:
            raise ValueError('Invalid host')
        return v

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)

global_host_whitelist = {'8.8.8.8', '127.0.0.1'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str = Depends(PingCommand.validate_host)):
    command = PingCommand(host)
    output = command.execute()
    return {'status': 'completed', 'output': output}