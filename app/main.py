from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent code injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    command = PingCommand(host)
    result = command.run()
    return {'status': 'completed', 'output': result.stdout}