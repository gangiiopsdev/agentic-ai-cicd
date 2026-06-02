from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self):
        if not self.host.isalnum():
            raise ValueError('Invalid input for host')

    def run_command(self):
        self.validate_host()
        result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    return command.run_command()