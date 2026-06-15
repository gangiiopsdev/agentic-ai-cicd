from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> dict:
        command_parts = ['ping', shlex.quote(self.host)]
        try:
            result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()