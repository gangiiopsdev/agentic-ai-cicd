from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def validate(self):
        if self.host.startswith('-') or ' ' in self.host or ';' in self.host:
            raise ValueError('Invalid input detected')

    def execute(self):
        args = ['ping', self.host]
        subprocess.call(args)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    command.validate()
    command.execute()
    return {'status': 'completed'}