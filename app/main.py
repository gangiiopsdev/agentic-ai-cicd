from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

class PingRouter:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        command = PingCommand(host)
        return {'status': 'completed', 'output': command.execute()}

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    response = PingRouter.ping(host)
    return response