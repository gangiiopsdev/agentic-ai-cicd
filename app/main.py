from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation
        args = ['ping', self.host]
        subprocess.run(args, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    try:
        result = command.execute()
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}