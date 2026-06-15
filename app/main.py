from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'

class PingEndpoint:
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
def ping_endpoint(host: str):
    return PingEndpoint.ping(host)