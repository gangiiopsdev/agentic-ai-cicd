from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', '-c', '1'] + shlex.split(self.host))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'result': result}