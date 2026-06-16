from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid host name')
    command = PingCommand(host)
    try:
        result = command.execute()
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}