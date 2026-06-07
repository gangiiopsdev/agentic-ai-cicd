from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Use shlex to safely escape the command arguments
            result = subprocess.run(shlex.split(f'ping {self.host}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # More comprehensive input sanitization
    if not host.isalnum() or '>' in host or '<' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    command_executor = PingCommand(host)
    return command_executor.execute()