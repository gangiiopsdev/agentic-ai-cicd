from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation with input validation
        if not self.host.strip():
            raise ValueError('Host parameter is required and cannot be empty')
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f'Ping command failed: {e}')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command_executor = PingCommand(host)
    response = command_executor.execute()
    return {'status': 'completed', 'output': response}