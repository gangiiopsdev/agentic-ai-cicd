from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '-' not in host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    ping_command = PingCommand(host)
    return ping_command.run()